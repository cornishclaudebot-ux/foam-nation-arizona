import subprocess, os, shutil
IMG=os.path.expanduser("~/foam-nation-site/img")
photos=["fn-03","fn-26","fn-24","fn-13","fn-21","fn-07","fn-31"]
CLIP=4.0; XF=0.8; FPS=30
tmp="/tmp/kb"; shutil.rmtree(tmp,ignore_errors=True); os.makedirs(tmp)
clips=[]
for i,p in enumerate(photos):
    src=f"{IMG}/{p}.jpg"
    if not os.path.exists(src): print("MISSING",src); continue
    out=f"{tmp}/c{i}.mp4"; d=int(CLIP*FPS)
    if i%2==0:
        z="z='min(zoom+0.0006,1.14)'"
    else:
        z="z='if(eq(on,0),1.14,max(zoom-0.0006,1.0))'"
    vf=(f"scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080,"
        f"zoompan={z}:d={d}:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1280x720:fps={FPS},format=yuv420p")
    # -t AFTER -i  => caps OUTPUT to CLIP seconds (the fix)
    cmd=["ffmpeg","-y","-loop","1","-framerate",str(FPS),"-i",src,"-vf",vf,
         "-t",str(CLIP),"-r",str(FPS),"-c:v","libx264","-preset","medium","-crf","24","-an",out]
    r=subprocess.run(cmd,capture_output=True,text=True)
    if r.returncode!=0: print("ERR clip",p,r.stderr[-500:]); raise SystemExit(1)
    dur=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],capture_output=True,text=True).stdout.strip()
    print(f"clip {p}: {dur}s"); clips.append(out)
inputs=[]
for c in clips: inputs+=["-i",c]
fc=[]; prev="0:v"; off=CLIP-XF
for i in range(1,len(clips)):
    lbl=f"v{i}"; fc.append(f"[{prev}][{i}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}[{lbl}]")
    prev=lbl; off+=CLIP-XF
out=f"{IMG}/hero.mp4"
cmd=["ffmpeg","-y"]+inputs+["-filter_complex",";".join(fc),"-map",f"[{prev}]",
     "-c:v","libx264","-preset","medium","-crf","25","-pix_fmt","yuv420p","-movflags","+faststart","-r",str(FPS),"-an",out]
r=subprocess.run(cmd,capture_output=True,text=True)
if r.returncode!=0: print("ERR xfade",r.stderr[-800:]); raise SystemExit(1)
sz=os.path.getsize(out)/1e6
dur=subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",out],capture_output=True,text=True).stdout.strip()
print(f"\nWROTE {out}  {sz:.1f} MB  duration={dur}s")

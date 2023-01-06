import os

pth = "D:/jvetlog"

txtlist = os.listdir(pth)
for txt in txtlist:
    txtpth = pth + '/' + txt
    name = txtpth.find('_')
    name = txtpth[:name]

    t = open(txtpth, "r")
    arr = []
    while True:
        line = t.readline()
        if not line: break

        if "POC" in line:
            if "POC   80" in line: break
            poc = line[6:8]
            psnr = line.find("[Y")
            psnr = line[psnr+3:psnr+8]
            qp = line.find('nQP')
            qp = line[qp+4:qp+7]
            arr.append((poc, psnr, qp))

    arr.sort(key=lambda x:x[0])
    save = open(name + '.txt', "w")

    for p, ps in arr:
        save.write(f"{p} {ps}\n")

    save.close()
    t.close()
    arr = []




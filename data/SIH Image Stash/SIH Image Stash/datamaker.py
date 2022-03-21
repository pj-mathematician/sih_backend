import json
d = {'Cars': {'sedans': ['https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/XY0lnP6.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/XY0lnP6.jpg', 'https://i.imgur.com/BTacI41.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/XY0lnP6.jpg', 'https://i.imgur.com/BTacI41.jpg', 'https://i.imgur.com/NdowwBe.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/XY0lnP6.jpg', 'https://i.imgur.com/BTacI41.jpg', 'https://i.imgur.com/NdowwBe.jpg', 'https://i.imgur.com/LyLXYk8.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/XY0lnP6.jpg', 'https://i.imgur.com/BTacI41.jpg', 'https://i.imgur.com/NdowwBe.jpg', 'https://i.imgur.com/LyLXYk8.jpg', 'https://i.imgur.com/3zeJAYx.jpg', 'https://i.imgur.com/JgxpyZO.jpg', 'https://i.imgur.com/ecMop22.jpg', 'https://i.imgur.com/XY0lnP6.jpg', 'https://i.imgur.com/BTacI41.jpg', 'https://i.imgur.com/NdowwBe.jpg', 'https://i.imgur.com/LyLXYk8.jpg', 'https://i.imgur.com/3zeJAYx.jpg', 'https://i.imgur.com/JdTIvXv.jpg'], 'suv': ['https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/OwinWGd.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/OwinWGd.jpg', 'https://i.imgur.com/7vGqYQM.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/OwinWGd.jpg', 'https://i.imgur.com/7vGqYQM.jpg', 'https://i.imgur.com/ffIuf4L.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/OwinWGd.jpg', 'https://i.imgur.com/7vGqYQM.jpg', 'https://i.imgur.com/ffIuf4L.jpg', 'https://i.imgur.com/cybFvYw.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/OwinWGd.jpg', 'https://i.imgur.com/7vGqYQM.jpg', 'https://i.imgur.com/ffIuf4L.jpg', 'https://i.imgur.com/cybFvYw.jpg', 'https://i.imgur.com/yxv3MVI.jpg', 'https://i.imgur.com/uk9M5iO.jpg', 'https://i.imgur.com/WFI0BKM.jpg', 'https://i.imgur.com/OFapzQL.jpg', 'https://i.imgur.com/jpPxZ2w.jpg', 'https://i.imgur.com/OwinWGd.jpg', 'https://i.imgur.com/7vGqYQM.jpg', 'https://i.imgur.com/ffIuf4L.jpg', 'https://i.imgur.com/cybFvYw.jpg', 'https://i.imgur.com/yxv3MVI.jpg', 'https://i.imgur.com/xEEmrHO.jpg']}, 'Indian Food': {'main course': ['https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/zT11Oxc.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/zT11Oxc.jpg', 'https://i.imgur.com/OhNOTd2.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/zT11Oxc.jpg', 'https://i.imgur.com/OhNOTd2.jpg', 'https://i.imgur.com/C1CYP6b.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/zT11Oxc.jpg', 'https://i.imgur.com/OhNOTd2.jpg', 'https://i.imgur.com/C1CYP6b.jpg', 'https://i.imgur.com/DqZGMip.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/zT11Oxc.jpg', 'https://i.imgur.com/OhNOTd2.jpg', 'https://i.imgur.com/C1CYP6b.jpg', 'https://i.imgur.com/DqZGMip.jpg', 'https://i.imgur.com/yXo3lbT.jpg', 'https://i.imgur.com/gsYsb1r.jpg', 'https://i.imgur.com/TjqpzmH.jpg', 'https://i.imgur.com/ymt3feD.jpg', 'https://i.imgur.com/zT11Oxc.jpg', 'https://i.imgur.com/OhNOTd2.jpg', 'https://i.imgur.com/C1CYP6b.jpg', 'https://i.imgur.com/DqZGMip.jpg', 'https://i.imgur.com/yXo3lbT.jpg', 'https://i.imgur.com/iZN41Kj.jpg'], 'snacks': ['https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/jj2lQjs.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/jj2lQjs.jpg', 'https://i.imgur.com/eryNV04.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/jj2lQjs.jpg', 'https://i.imgur.com/eryNV04.jpg', 'https://i.imgur.com/SoxLypk.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/jj2lQjs.jpg', 'https://i.imgur.com/eryNV04.jpg', 'https://i.imgur.com/SoxLypk.jpg', 'https://i.imgur.com/soDbb9c.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/jj2lQjs.jpg', 'https://i.imgur.com/eryNV04.jpg', 'https://i.imgur.com/SoxLypk.jpg', 'https://i.imgur.com/soDbb9c.jpg', 'https://i.imgur.com/UWWGFUP.jpg', 'https://i.imgur.com/fpj7wpm.jpg', 'https://i.imgur.com/ZMHzS6O.jpg', 'https://i.imgur.com/bo7toVG.jpg', 'https://i.imgur.com/jj2lQjs.jpg', 'https://i.imgur.com/eryNV04.jpg', 'https://i.imgur.com/SoxLypk.jpg', 'https://i.imgur.com/soDbb9c.jpg', 'https://i.imgur.com/UWWGFUP.jpg', 'https://i.imgur.com/wYfreml.jpg']}, 'Pets': {'cats': ['https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/Ui9UeK4.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/Ui9UeK4.jpg', 'https://i.imgur.com/49HGho6.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/Ui9UeK4.jpg', 'https://i.imgur.com/49HGho6.jpg', 'https://i.imgur.com/71TyOp6.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/Ui9UeK4.jpg', 'https://i.imgur.com/49HGho6.jpg', 'https://i.imgur.com/71TyOp6.jpg', 'https://i.imgur.com/dvLqXfq.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/Ui9UeK4.jpg', 'https://i.imgur.com/49HGho6.jpg', 'https://i.imgur.com/71TyOp6.jpg', 'https://i.imgur.com/dvLqXfq.jpg', 'https://i.imgur.com/ibGnCHD.jpg', 'https://i.imgur.com/yV5KnFO.jpg', 'https://i.imgur.com/mjLx1Pf.jpg', 'https://i.imgur.com/wApY2sv.jpg', 'https://i.imgur.com/Ui9UeK4.jpg', 'https://i.imgur.com/49HGho6.jpg', 'https://i.imgur.com/71TyOp6.jpg', 'https://i.imgur.com/dvLqXfq.jpg', 'https://i.imgur.com/ibGnCHD.jpg', 'https://i.imgur.com/bIpWZwC.jpg'], 'dogs': ['https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/NICSjPH.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/NICSjPH.jpg', 'https://i.imgur.com/G5P6f58.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/NICSjPH.jpg', 'https://i.imgur.com/G5P6f58.jpg', 'https://i.imgur.com/IGUnfa1.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/NICSjPH.jpg', 'https://i.imgur.com/G5P6f58.jpg', 'https://i.imgur.com/IGUnfa1.jpg', 'https://i.imgur.com/t2wOpXH.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/NICSjPH.jpg', 'https://i.imgur.com/G5P6f58.jpg', 'https://i.imgur.com/IGUnfa1.jpg', 'https://i.imgur.com/t2wOpXH.jpg', 'https://i.imgur.com/OAXfHKz.jpg', 'https://i.imgur.com/a1vu2c5.jpg', 'https://i.imgur.com/pVWt4ev.jpg', 'https://i.imgur.com/sOfMduJ.jpg', 'https://i.imgur.com/NICSjPH.jpg', 'https://i.imgur.com/G5P6f58.jpg', 'https://i.imgur.com/IGUnfa1.jpg', 'https://i.imgur.com/t2wOpXH.jpg', 'https://i.imgur.com/OAXfHKz.jpg', 'https://i.imgur.com/jnsSlX7.jpg']}}
main = {}
iter = 0
for i in d:
    main[i]={}
    for j in d[i]:
        main[i][j]={}
        for k in d[i][j]:
            main[i][j]["image_{}".format(iter)] = k
            iter += 1
# write main dictionary to a text file
with open('main.txt', 'w') as f:
    json.dump(main, f)


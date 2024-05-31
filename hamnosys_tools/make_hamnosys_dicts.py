import json

hamnosys = "{}|,.?"

hamtext = "hamfist,hamflathand,hamfinger2,hamfinger23,hamfinger23spread,hamfinger2345,hampinch12,hampinchall,hampinch12open,hamcee12,hamceeall,hamceeopen,hamthumboutmod,hamthumbacrossmod,hamthumbopenmod,hamlargemod,hamdoublebent,hamfingerstraightmod,hamfingerbendmod,hamfingerhookmod,hamdoublehooked,hamthumb,hamindexfinger,hammiddlefinger,hamringfinger,hampinky,hambetween,hamfingertip,hamfingernail,hamfingerpad,hamfingermidjoint,hamfingerbase,hamfingerside,hamextfingeru,hamextfingerur,hamextfingerr,hamextfingerdr,hamextfingerd,hamextfingerdl,hamextfingerl,hamextfingerul,hamextfingero,hamextfingeror,hamextfingerol,hamextfingeril,hamextfingeri,hamextfingerir,hamextfingerui,hamextfingeruo,hamextfingerdi,hamextfingerdo,hamextfingero,hamextfingeri,hampalmu,hampalmur,hampalmr,hampalmdr,hampalmd,hampalmdl,hampalml,hamorirelative,hamheadtop,hamhead,hamforehead,hamnose,hamnostrils,hamlips,hamtongue,hamteeth,hamchin,hamunderchin,hamneck,hamshouldertop,hamshoulders,hamchest,hamstomach,hambelowstomach,hameyebrows,hameyes,hamear,hamearlobe,hamcheek,hamupperarm,hamelbowinside,hamlowerarm,hamwristback,hamthumbball,hampalm,hamhandback,hamthumbside,hampinkyside,hamthumb,hamindexfinger,hammiddlefinger,hamringfinger,hampinky,hambetween,hamfingertip,hamfingerpad,hamfingermidjoint,hamfingerbase,hamclose,hamtouch,haminterlock,hamcross,hambrushing,hambehind,hamarmextended,hamlrbeside,hamlrat,hamdoublebent,hamdoublehooked,hamneutralspace,hammoveu,hammoveur,hammover,hammovedr,hammoved,hammovedl,hammovel,hammoveul,hammoveo,hammoveor,hammoveol,hammoveil,hammovei,hammoveir,hammoveuo,hammoveui,hammovedi,hammovedo,hamfast,hamslow,hamtense,hamrest,hamhalt,hamrepeatfromstart,hamrepeatfromstartseveral,hamrepeatcontinue,hamrepeatcontinueseveral,hamrepeatreverse,hamsmallmod,hamlargemod,hamnomotion,hamincreasing,hamdecreasing,hamarcl,hamarcu,hamarcd,hamarcr,hamwavy,hamellipsev,hamellipseur,hamellipseh,hamellipseul,hamzigzag,hamcircleu,hamcircleur,hamcircler,hamcircledr,hamcircled,hamcircledl,hamcirclel,hamcircleul,hamcircleo,hamcircleor,hamcircler,hamcircleir,hamcirclei,hamcircleil,hamcirclel,hamclocku,hamclockur,hamclockr,hamclockdr,hamclockd,hamclockdl,hamclockl,hamclockul,hamclockfull,hamcircleu,hamcircleuo,hamcircleo,hamcircledo,hamcircled,hamcircledi,hamcirclei,hamcircleui,hamstircw,hamnodding,hamtwisting,hamreplace,hamstirccw,hamswinging,hamfingerplay,hambetween,hamsymmpar,hamsymmlr,hamfingerstraightmod,hamlargemod,hamsymmlr,hamfingerstraightmod,hamlargemod,hamparbegin,hamplus,hamparend,hamalternatingmotion,hamnonipsi,hamnondominant,hametc,hamseqbegin,hamseqend,hamparbegin,hamparend,hamfusionbegin,hamfusionend,hamaltbegin,hamaltend,hammetaalt,hamcoreftag,hamcorefref,hamthumb,hamindexfinger,hammiddlefinger,hamringfinger,hampinky,hamcomma,hamfullstop,hamquery,hammime"

id_to_symbol = {}

symbol_to_id = {}

hamt = hamtext.split(",")
for i in range(len(hamnosys)):
	id_to_symbol[hamt[i]] = hamnosys[i]
	symbol_to_id[hamnosys[i]] = hamt[i]

json.dump(id_to_symbol, open("id_to_hamnosys_map.json","w"))
json.dump(symbol_to_id, open("hamnosys_to_id_map.json","w"))


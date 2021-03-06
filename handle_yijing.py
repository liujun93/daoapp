import pandas as pd

guas = \
'''乾
﹝乾上．乾下﹞ 元．亨．利．贞．
彖曰．大哉乾元，万物资始，乃统天。云行雨施，品物流形。大明终始，六位时成。时乘六龙以御天。乾道变化，各正性命。保合大和，乃利贞。首出庶物，万国咸宁。
象曰．天行健，君子以自强不息。“潜龙勿用”，阳在下也。“见龙在田”，德施普也。“终日乾乾”，反复道也。“或跃在渊”，进无咎也。“飞龙在天”，大人造也。“亢龙有悔”，盈不可久也。“用九”，天德不可为首也。

坤
﹝坤上．坤下﹞ 元亨．利牝马之贞．君子有攸往．先迷．后得主利．西南得朋．东北丧朋．安贞吉．
彖曰．至哉坤元．万物资生．乃顺承天．坤厚载物．德合无疆．含弘光大．品物咸亨．牝马地类．行地无疆．柔顺利贞．君子攸行．先迷失道．后顺得常．西南得朋．乃与类行．东北丧朋．乃终有庆．安贞之吉．应地无疆．
象曰．地势坤．君子以厚德载物．

屯
﹝坎上．震下﹞ 元亨．利贞．勿用有攸往．利建侯．
彖曰．屯．刚柔始交而难生．动乎险中．大亨贞．雷雨之动满盈．天造草昧．宜建侯而不宁．
象曰．云雷屯．君子以经纶．  

蒙
（艮上．坎下﹞ 亨．匪我求童蒙．童蒙求我．初筮告．再三渎．渎则不告．利贞．
彖曰．蒙．山下有险．险而止蒙．蒙亨．以亨行．时中也．匪我求童蒙．童蒙求我．志应也．初筮告．以刚中也．再三渎．渎则不告．渎蒙也．蒙以养正．圣功也．
象曰．山下出泉．蒙．君子以果行育德．  

需
﹝坎上．乾下﹞ 有孚．光亨贞吉．利涉大川．
彖曰．需．须也．险在前也．刚健而不陷．其义不困穷矣．需有孚．光亨贞吉．位乎天位．以正中也．利涉大川．往有功也．
象曰．云上于天．需．君子以饮食宴乐．  

讼
﹝乾上．坎下﹞ 有孚．窒惕．中吉．终凶．利见大人．不利涉大川．
彖曰．讼．上刚下险．险而健．讼．讼有孚窒惕中吉．刚来而得中也．终凶．讼不可成也．利见大人．尚中正也．不利涉大川．入于渊也．
象曰．天与水违行．讼．君子以作事谋始  

师
﹝坤上．坎下﹞ 贞．丈人．吉．无咎．
彖曰．师．众也．贞．正也．能以众正．可以王矣．刚中而应．行险而顺．以此毒天下．而民从之．吉又何咎矣．
象曰．地中有水．师．君子以容民畜众．  

比
﹝坎上．坤下﹞ 吉．原筮．元永贞．无咎．不宁方来．后夫凶．
彖曰．比吉也．比．辅也．下顺从也．原筮元永贞无咎．以刚中也．不宁方来．上下应也．后夫凶．其道穷也．
象曰．地上有水．比．先王以建万国．亲诸侯．  

小畜
﹝巽上．乾下﹞ 亨．密云不雨．自我西郊．
彖曰．小畜．柔得位而上下应之曰小畜．健而巽．刚中而志行．乃亨．密云不雨．尚往也．自我西郊．施未行也．
象曰．风行天上．小畜．君子以懿文德．  

履
﹝乾上．兑下﹞ 虎尾．不咥人．亨．
彖曰．履．柔履刚也．说而应乎乾．是以履虎尾．不咥人亨．刚正中．履帝位而不疚．光明也．
象曰．上天下泽履．君子以辩上下．定民志．  

泰
﹝坤上．乾下﹞ 小往大来．吉亨．
彖曰．泰．小往大来吉亨．则是天地交而万物通也．上下交而其志同也．内阳而外阴．内健而外顺．内君子而外小人．君子道长．小人道消也．
象曰．天地交．泰．后以财成天地之道．辅相天地之宜．以左右民．  

否
﹝乾上．坤下﹞ 之匪人．不利君子贞．大往小来．
彖曰．否之匪人．不利君子贞．大往小来．则是天地不交而万物不通也．上下不交而天下无邦也．内阴而外阳．内柔而外刚．内小人而外君子．小人道长．君子道消也．
象曰．天地不交．否．君子以俭德辟难．不可荣以禄．  

同人
﹝乾上．离下﹞ 于野．亨．利涉大川．利君子贞．
彖曰．同人．柔得位得中而应乎乾．曰同人．同人曰．同人于野亨．利涉大川．乾行也．文明以健．中正而应．君子正也．唯君子为能通天下之志．
象曰．天与火．同人．君子以类族辨物．  

大有
﹝离上．乾下﹞ 元亨．
彖曰．大有．柔得尊位大中．而上下应之曰大有．其德刚健而文明．应乎天而时行．是以元亨．
象曰．火在天上．大有．君子以遏恶扬善．顺天休命．  

谦
﹝坤上．艮下﹞ 亨．君子有终．
彖曰．谦亨．天道下济而光明．地道卑而上行．天道亏盈而益谦．地道变盈而流谦．鬼神害盈而福谦．人道恶盈而好谦．谦尊而光．卑而不可逾．君子之终也．
象曰．地中有山．谦．君子以裒多益寡．称物平施．  

豫
﹝震上．坤下﹞ 利建侯行师．
彖曰．豫．刚应而志行．顺以动．豫．豫顺以动．故天地如之．而况建侯行师乎．天地以顺动．故日月不过．而四时不忒．圣人以顺动．则刑罚清而民服．豫之时义大矣哉．
象曰．雷出地奋．豫．先王以作乐崇德．殷荐之上帝．以配祖考．  

随
﹝兑上．震下﹞ 元亨利贞．无咎．
彖曰．随．刚来而下柔．动而说．随．大亨贞无咎．而天下随时．随时之义大矣哉．
象曰．泽中有雷．随．君子以向晦入宴息．  

蛊
﹝艮上．巽下﹞ 元亨．利涉大川．先甲三日．后甲三日．
彖曰．蛊．刚上而柔下．巽而止．蛊．蛊元亨而天下治也．利涉大川．往有事也．先甲三日．后甲三日．终则有始．天行也．
象曰．山下有风．蛊．君子以振民育德．  

临
﹝坤上．兑下﹞ 元亨．利贞．至于八月有凶．
彖曰．临．刚浸而长．说而顺．刚中而应．大亨以正．天之道也．至于八月有凶．消不久也．
象曰．泽上有地．临．君子以教思无穷．容保民无疆．  

观
﹝巽上．坤下﹞ 盥而不荐．有孚颙若．
彖曰．大观在上．顺而巽．中正以观天下．观盥而不荐．有孚颙若．下观而化也．观天之神道．而四时不忒．圣人以神道设教．而天下服矣．
象曰．风行地上．观．先王以省方观民设教．  

噬嗑
﹝离上．震下﹞ 亨．利用狱．
彖曰．颐中有物．曰噬嗑．噬嗑而亨．刚柔分动而明．雷电合而章．柔得中而上行．虽不当位．利用狱也．
象曰．雷电．噬嗑．先王以明罚徕法．  

贲
﹝艮上．离下﹞ 亨．小利有攸往．
彖曰．贲亨．柔来而文刚．故亨．分刚上而文柔．故小利有攸往．天文也．文明以止．人文也．观乎天文．以察时变．观乎人文．以化成天下．
象曰．山下有火．贲．君子以明庶政．无敢折狱  

剥
﹝艮上．坤下﹞ 不利有攸往．
彖曰．剥．剥也．柔变刚也．不利有攸往．小人长也．顺而止之．观象也．君子尚消息盈虚．天行也．
象曰．山附于地．剥．上以厚下安宅．  

复
﹝坤上．震下﹞ 亨．出入无疾．朋来无咎．反复其道．七日来复．利有攸往．
彖曰．复亨．刚反．动而以顺行．是以出入无疾．朋来无咎．反复其道．七日来复．天行也．利有攸往．刚长也．复其见天地之心乎．
象曰．雷在地中．复．先王以至日闭关．商旅不行．后不省方．  

无妄
﹝乾上．震下﹞ 元亨．利贞．其匪正有眚．不利有攸往．
彖曰．无妄．刚自外来．而为主于内．动而健．刚中而应．大亨以正．天之命也．其匪正有眚．不利有攸往．无妄之往．何之矣．天命不佑．行矣哉．
象曰．天下雷行．物与无妄．先王以茂对时育万物．  

大畜
﹝艮上．乾下﹞ 利贞．不家食吉．利涉大川．
彖曰．大畜．刚健笃实辉光．日新其德．刚上而尚贤．能止健．大正也．不家食吉．养贤也．利涉大川．应乎天也．
象曰．天在山中．大畜．君子以多识前言往行．以畜其德．  

颐
﹝艮上．震下﹞ 贞吉．观颐．自求口实．
彖曰．颐．贞吉．养正则吉也．观颐．观其所养也．自求口实．观其自养也．天地养万物．圣人养贤以及万民．颐之时义大矣哉．
象曰．山下有雷．颐．君子以慎言语．节饮食．  

大过
﹝兑上．巽下﹞ 栋挠．利有攸往．亨．
彖曰．大过．大者过也．栋挠本末弱也．刚过而中．巽而说行．利有攸往．乃亨．大过之时大矣哉．
象曰．泽灭木．大过．君子以独立不惧．遯世无闷．  

坎
﹝坎上．坎下﹞ 习坎．有孚．维心亨．行有尚．
彖曰．习坎．重险也．水流而不盈．行险而不失其信．维心亨．乃以刚中也．行有尚．往有功也．天险不可升也．地险山川丘陵也．王公设险以守其国．险之时用大矣哉．
象曰．水洊至．习坎．君子以常德行．习教事．  

离
﹝离上．离下﹞ 利贞．亨．畜牝牛．吉．
彖曰．离．丽也．日月丽乎天．百谷草木丽乎土．重明以丽乎正．乃化成天下．柔丽乎中正．故亨．是以畜牝牛吉也．
象曰．明两作离．大人以继明照于四方．  

咸
﹝兑上．艮下﹞ 亨．利贞．取女吉．
彖曰．咸．感也．柔上而刚下．二气感应以相与．止而说．男下女．是以亨利贞．取女吉也．天地感．而万物化生．圣人感人心．而天下和平．观其所感而天地万物之情可见矣．
象曰．山上有泽．咸．君子以虚受人．  

恒
（震上巽下）恒亨无咎利贞利有攸往。
彖曰．恒．久也．刚上而柔下．雷风相与．巽而动．刚柔皆应．恒．恒亨无咎．利贞．久于其道也．天地之道．恒久而不已也．利有攸往．终则有始也．日月得天．而能久照．四时变化．而能久成．圣人久于其道．而天下化成．观其所恒．而天地万物之情可见矣．
象曰．雷风．恒．君子以立不易方．  

遁
﹝乾上．艮下﹞ 亨．小利贞．
彖曰．遁亨．遁而亨也．刚当位而应．与时行也．小利贞．浸而长也．遁之时义大矣哉．
象曰．天下有山．遁．君子以远小人．不恶而严．  

大壮
﹝震上．乾下﹞ 利贞．
彖曰．大壮．大者壮也．刚以动．故壮．大壮利贞．大者正也．正大．而天地之情可见矣．
象曰．雷在天上．大壮．君子以非礼弗履．  

晋
﹝离上．坤下﹞ 康侯用锡马蕃庶．昼日三接．
彖曰．晋．进也．明出地上．顺而丽乎大明．柔进而上行．是以康侯用锡马蕃庶．昼日三接也．
象曰．明出地上．晋．君子以自昭明德．  

明夷
﹝坤上．离下﹞ 利艰贞．
彖曰．明入地中．明夷．内文明而外柔顺．以蒙大难．文王以之．利艰贞．晦其明也．内难而能正其志．箕子以之．
象曰．明入地中．明夷．君子以莅众．用晦而明．  

家人
﹝巽上．离下﹞ 利女贞．
彖曰．家人．女正位乎内．男正位乎外．男女正．天地之大义也．家人有严君焉．父母之谓也．父父．子子．兄兄．弟弟．夫夫．妇妇．而家道正．正家．而天下定矣．
象曰．风自火出．家人．君子以言有物．而行有恒．  

睽
﹝离上．兑下﹞ 小事吉．
彖曰．睽．火动而上．泽动而下．二女同居．其志不同行．说而丽乎明．柔进而上行．得中而应乎刚．是以小事吉．天地睽．而其事同也．男女睽．而其志通也．万物睽．而其事类也．睽之时用大矣哉．
象曰．上火下泽．睽．君子以同而异．  

蹇
﹝坎上．艮下﹞ 利西南．不利东北．利见大人．贞吉．
彖曰．蹇．难也．险在前也．见险而能止．知矣哉．蹇．利西南．往得中也．不利东北．其道穷也．利见大人．往有功也．当位贞吉．以正邦也．蹇之时用大矣哉．
象曰．山上有水．蹇．君子以反身修德．  

解
﹝震上．坎下﹞ 利西南．无所往．其来复吉．有攸往．夙吉．
彖曰．解．险以动．动而免乎险．解．解利西南．往得众也．其来复吉．乃得中也．有攸往夙吉．往有功也．天地解．而雷雨作．雷雨作．而百果草木皆甲坼．解之时大矣哉．
象曰．雷雨作解．君子以赦过宥罪．  

损
﹝艮上．兑下﹞ 有孚．元吉．无咎可贞．利有攸往．曷之用．二簋可用享．
彖曰．损．损下益上．其道上行．损而有孚．元吉．无咎．可贞．利有攸往．曷之用．二簋可用享．二簋应有时．损刚益柔有时．损益盈虚．与时偕行．
象曰．山下有泽．损．君子以惩忿窒欲．  

益
﹝巽上．震下﹞ 利有攸往．利涉大川．
彖曰．益．损上益下．民说无疆．自上下下．其道大光．利有攸往．中正有庆．利涉大川．木道乃行．益动而巽．日进无疆．天施地生．其益无方．凡益之道．与时偕行．
象曰．风雷益．君子以见善则迁．有过则改．  

夬
﹝兑上．乾下﹞ 扬于王庭．孚号有厉．告自邑．不利即戎．利有攸往．
彖曰．夬．决也．刚决柔也．健而说．决而和．扬于王庭．柔乘五刚也．孚号有厉．其危乃光也．告自邑．不利即戎．所尚乃穷也．利有攸往．刚长乃终也．
象曰．泽上于天．夬．君子以施禄及下．居德则忌．  

姤
﹝乾上．巽下﹞ 女壮．勿用取女．
彖曰．姤．遇也．柔遇刚也．勿用取女．不可与长也．天地相遇．品物咸章也．刚遇中正．天下大行也．姤之时义大矣哉．
象曰．天下有风．姤．后以施命诰四方  

萃
﹝兑上．坤下﹞ 亨．王假有庙．利见大人．亨．利贞．用大牲．吉．利有攸往．
彖曰．萃．聚也．顺以说．刚中而应．故聚也．王假有庙．致孝享也．利见大人亨．聚以正也．用大牲吉．利有攸往．顺天命也．观其所聚．而天地万物之情可见矣．
象曰．泽上于地．萃．君子以除戎器．戒不虞．  

升
﹝坤上．巽下﹞ 元亨．用见大人．勿恤．南征吉．
彖曰．柔以时升．巽而顺．刚中而应．是以大亨．用见大人．勿恤．有庆也．南征吉．志行也．
象曰．地中生木．升．君子以顺德．积小以高大．  

困
﹝兑上．坎下﹞ 亨．贞大人吉．无咎．有言不信．
彖曰．困．刚揜也．险以说．困而不失其所享．其唯君子乎．贞大人吉．以刚中也．有言不信．尚口乃穷也．
象曰．泽无水．困．君子以致命遂志．  

井
﹝坎上．巽下﹞ 改邑不改井．无丧无得．往来井井．汔至亦未繘井．羸其瓶．凶．
彖曰．巽乎水而上水．井．井养而不穷也．改邑不改井．乃以刚中也．汔至亦未繘井．未有功也．羸其瓶．是以凶也．
象曰．木上有水．井．君子以劳民劝相．  

革
﹝兑上．离下﹞ 已日乃孚．元亨．利贞．悔亡．
彖曰．革．水火相息．二女同居．其志不相得．曰革．已日乃孚．革而信之．文明以说．大亨以正．革而当．其悔乃亡．天地革而四时成．汤武革命．顺乎天而应乎人．革之时大矣哉．
象曰．泽中有火．革．君子以治历明时．  

鼎
﹝离上．巽下﹞ 元吉．亨．
彖曰．鼎．象也．以木巽火．亨饪也．圣人亨以享上帝．而大亨以养圣贤．巽而耳目聪明．柔进而上行．得中而应乎刚．是以元亨．
象曰．木上有火．鼎．君子以正位凝命．  

震
﹝震上．震下﹞ 亨．震来虩虩．笑言哑哑．震惊百里．不丧匕鬯．
彖曰．震亨．震来虩虩．恐致福也．笑言哑哑．后有则也．震惊百里．惊远而惧迩也．出可以守宗庙社稷．以为祭主也．
象曰．洊雷震．君子以恐惧修省．  

艮
﹝艮上．艮下﹞ 其背．不获其身．行其庭．不见其人．无咎．
彖曰．艮．止也．时止则止．时行则行．动静不失其时．其道光明．艮其止．止其所以．上下敌应．不相与也．是以不获其身．行其庭．不见其人．无咎也．
象曰．兼山．艮．君子以思不出其位．  

渐
﹝巽上．艮下﹞ 女归吉．利贞．
彖曰．渐．之进也．女归吉也．进得位．往有功也．进以正．可以正邦也．其位．刚得中也．止而巽．动不穷也．
象曰．山上有木．渐．君子以居贤德善俗．  

归妹
﹝震上．兑下﹞ 征凶无攸利．
彖曰．归妹．天地之大义也．天地不交．而万物不兴．归妹．人之终始也．说以动．所归妹也．征凶．位不当也．无攸利．柔乘刚也．
象曰．泽上有雷．归妹．君子以永终知敝．  

丰
﹝震上．离下﹞ 亨．王假之．勿忧．宜日中．
彖曰．丰．大也．明以动．故丰．王假之．尚大也．勿忧宜日中．宜照天下也．日中则昃．月盈则食．天地盈虚．与时消息．而况于人乎．况于鬼神乎．
象曰．雷电皆至．丰．君子以折狱致刑．  

旅
﹝离上．艮下﹞ 小亨．旅贞吉．
彖曰．旅小亨．柔得中乎外而顺乎刚．止而丽乎明．是以小亨旅贞吉也．旅之时义大矣哉．
象曰．山上有火．旅．君子以明慎用刑．而不留狱．  

巽
﹝巽上．巽下﹞ 小亨．利有攸往．利见大人．
彖曰．重巽以申命．刚巽乎中正．而志行．柔皆顺乎刚．是以小亨．利有攸往．利见大人．
象曰．随风．巽．君子以申命行事．  

兑
﹝兑上．兑下﹞ 亨．利贞．
彖曰．兑．说也．刚中而柔外．说以利贞．是以顺乎天而应乎人．说以先民．民忘其劳．说以犯难．民忘其死．说之大．民劝矣哉．
象曰．丽泽．兑．君子以朋友讲习．  

涣
﹝巽上．坎下﹞ 亨．王假有庙．利涉大川．利贞．
彖曰．涣亨．刚来而不穷．柔得位乎外而上同．王假有庙．王乃在中也．利涉大川．乘木有功也．
象曰．风行水上．涣．先王以享于帝立庙．  

节
﹝坎上．兑下﹞ 亨．苦节不可贞．
彖曰．节亨．刚柔分而刚得中．苦节不可贞．其道穷也．说以行险．当位以节．中正以通．天地节而四时成．节以制度．不伤财．不害民．
象曰．泽上有水．节．君子以制数度．议德行．  

中孚
﹝巽上．兑下﹞ 豚鱼吉．利涉大川．利贞．
彖曰．中孚．柔在内而刚得中．说而巽．孚．乃化邦也．豚鱼吉．信及豚鱼也．利涉大川．乘木舟虚也．中孚以利贞．乃应乎天也．
象曰．泽上有风．中孚．君子以议狱缓死．  

小过
﹝震上．艮下﹞ 亨．利贞．可小事．不可大事．飞鸟遗之音．不宜上．宜下．大吉．
彖曰．小过．小者过而亨也．过以利贞．与时行也．柔得中．是以小事吉也．刚失位而不中．是以不可大事也．有飞鸟之象焉．飞鸟遗之音．不宜上．宜下．大吉．上逆而下顺也．
象曰．山上有雷．小过．君子以行过乎恭．丧过乎哀．用过乎俭．  

既济
﹝坎上．离下﹞ 亨小．利贞．初吉．终乱．
彖曰．既济亨．小者亨也．利贞．刚柔正而位当也．初吉．柔得中也．终止则乱．其道穷也．
象曰．水在火上．既济．君子以思患而豫防之．  

未济
﹝离上．坎下﹞ 亨．小狐汔济．濡其尾．无攸利．
彖曰．未济亨．柔得中也．小狐汔济．未出中也．濡其尾．无攸利．不续终也．虽不当位．刚柔应也．
象曰．火在水上．未济．君子以慎辨物居方．'''

df = pd.read_csv('易经/易经.csv', dtype=str).fillna('', inplace=False)

rdf = pd.DataFrame(columns=["序号","类型","名称","拼音","二进制卦","卦象描述","卦象","象辞","卦辞","彖辞","彖辞2"])

rdf = rdf.append(df)

for gua in guas.split('\n\n'):
    name, guaci, tuanci, xiangci = gua.split('\n')
    idx = rdf[(rdf['名称']==name.strip()) & (rdf['类型']=='六十四卦')].index.values.tolist()[0]
    rdf.loc[idx, ["象辞", '卦辞', "彖辞2"]] = [(guaci[:8]+xiangci[3:]).strip(), guaci[8:].strip(), tuanci[3:].strip()]

rdf.to_csv('csv/易经.csv', header=1, index=0)
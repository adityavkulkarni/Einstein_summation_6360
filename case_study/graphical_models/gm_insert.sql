DROP TABLE IF EXISTS R0;
CREATE TEMPORARY TABLE R0 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R0 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (0, 6, 1.0), (1, 0, 1.0), (1, 1, 0.973682810549305), (1, 2, 0.9737521303611223), (1, 3, 1.0328467752662436), (1, 4, 1.0239713783621835), (1, 5, 0.6860998316497583), (1, 6, 1.0359792444484062);
DROP TABLE IF EXISTS R1;
CREATE TEMPORARY TABLE R1 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R1 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.7880266547431627), (1, 2, 1.0868802911571624);
DROP TABLE IF EXISTS R2;
CREATE TEMPORARY TABLE R2 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R2 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.8136311589694804), (1, 2, 1.2375921946213932);
DROP TABLE IF EXISTS R3;
CREATE TEMPORARY TABLE R3 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R3 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.7635736624896113), (1, 2, 4.25101470626053), (2, 0, 1.0), (2, 1, 0.5006963433012598), (2, 2, 5.754813352600789), (3, 0, 1.0), (3, 1, 0.3906909210403103), (3, 2, 0.8482647609756965), (4, 0, 1.0), (4, 1, 0.35162189765681234), (4, 2, 0.19037326949817904), (5, 0, 1.0), (5, 1, 0.7473860361321798), (5, 2, 0.5317221189323259);
DROP TABLE IF EXISTS R4;
CREATE TEMPORARY TABLE R4 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R4 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (0, 6, 1.0), (0, 7, 1.0), (0, 8, 1.0), (0, 9, 1.0), (0, 10, 1.0), (1, 0, 1.0), (1, 1, 0.9009636145834332), (1, 2, 1.0021732351669361), (1, 3, 1.044985465076018), (1, 4, 0.9980789072695513), (1, 5, 0.9638449018529875), (1, 6, 1.0121223877489265), (1, 7, 0.9895452051573524), (1, 8, 1.0461791698587772), (1, 9, 0.927770671202863), (1, 10, 0.9780939638483145), (2, 0, 1.0), (2, 1, 0.892449617631239), (2, 2, 0.911227275887941), (2, 3, 0.8443406765194539), (2, 4, 1.3213447385481847), (2, 5, 1.097364902179803), (2, 6, 1.2282697255302135), (2, 7, 0.990964446853202), (2, 8, 0.9190401041297751), (2, 9, 0.9097898819979845), (2, 10, 0.8923792934525435), (3, 0, 1.0), (3, 1, 0.9539708735547351), (3, 2, 0.9676830511255532), (3, 3, 1.0729559971035139), (3, 4, 1.1042625824391825), (3, 5, 1.4086222462701348), (3, 6, 1.3436317496879284), (3, 7, 1.0647951906091397), (3, 8, 1.0670156618121183), (3, 9, 0.8604621314387596), (3, 10, 0.9008776402921514), (4, 0, 1.0), (4, 1, 1.031830039975031), (4, 2, 0.8842242109247856), (4, 3, 1.1919261677475554), (4, 4, 1.0263485847181886), (4, 5, 1.1195461082267846), (4, 6, 1.2815272714594983), (4, 7, 0.8869026378527145), (4, 8, 0.9383175879317046), (4, 9, 1.0183319490198481), (4, 10, 0.9570430440459394), (5, 0, 1.0), (5, 1, 0.9746854610399724), (5, 2, 1.033056428279879), (5, 3, 0.993864266150039), (5, 4, 0.9715312661785909), (5, 5, 0.9174740948091671), (5, 6, 0.8969423331560604), (5, 7, 0.960805142109766), (5, 8, 1.0693233113349119), (5, 9, 0.9800707206184379), (5, 10, 0.9800796181459871);
DROP TABLE IF EXISTS R5;
CREATE TEMPORARY TABLE R5 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R5 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (0, 6, 1.0), (1, 0, 1.0), (1, 1, 0.8778384147098085), (1, 2, 0.9325574786317935), (1, 3, 1.0763465277837372), (1, 4, 1.0025681512920561), (1, 5, 0.8836638578123289), (1, 6, 1.008816810205954), (2, 0, 1.0), (2, 1, 1.0155693277972138), (2, 2, 0.872829122777219), (2, 3, 0.8260881074118583), (2, 4, 0.9347247721978448), (2, 5, 1.3075815117067313), (2, 6, 0.9346608152622072), (3, 0, 1.0), (3, 1, 1.0799057652369102), (3, 2, 0.8896655047107954), (3, 3, 1.132391721555868), (3, 4, 1.1299856835308513), (3, 5, 2.3246544996186453), (3, 6, 1.3412427457189036), (4, 0, 1.0), (4, 1, 0.8965838707335579), (4, 2, 1.0197321444366343), (4, 3, 1.124490465263779), (4, 4, 0.8777310473375994), (4, 5, 2.05564423182593), (4, 6, 1.3159804749593502), (5, 0, 1.0), (5, 1, 0.9662179110478596), (5, 2, 0.9819781501968057), (5, 3, 0.9252738483399526), (5, 4, 1.0548656107049006), (5, 5, 0.865590289417492), (5, 6, 0.8898389723743598);
DROP TABLE IF EXISTS R6;
CREATE TEMPORARY TABLE R6 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R6 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 1.0000206894466637), (1, 2, 0.9960876088232643), (2, 0, 1.0), (2, 1, 1.003595740699548), (2, 2, 1.0033806700650885), (3, 0, 1.0), (3, 1, 1.016838685499577), (3, 2, 1.019492965967967), (4, 0, 1.0), (4, 1, 1.0217286508361816), (4, 2, 1.003530043000048), (5, 0, 1.0), (5, 1, 0.9943436914868544), (5, 2, 0.9945395858155766);
DROP TABLE IF EXISTS R7;
CREATE TEMPORARY TABLE R7 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R7 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (1, 0, 1.0), (1, 1, 1.0759895260931363), (1, 2, 1.1047073294710485), (1, 3, 0.9120662129688796), (1, 4, 0.9648065721045944), (1, 5, 0.8123623134131202), (2, 0, 1.0), (2, 1, 0.7358991041295598), (2, 2, 1.3799630828766214), (2, 3, 1.233295506170814), (2, 4, 1.1286001971957602), (2, 5, 0.9946841027619808), (3, 0, 1.0), (3, 1, 1.1271316743710995), (3, 2, 2.085103705315591), (3, 3, 1.6867816120781278), (3, 4, 1.003798970297169), (3, 5, 1.1835121660137131), (4, 0, 1.0), (4, 1, 0.9998212318088034), (4, 2, 1.9671897503206537), (4, 3, 1.6918476153624729), (4, 4, 0.8935593954751399), (4, 5, 1.0133048541342489), (5, 0, 1.0), (5, 1, 0.9836901122072526), (5, 2, 0.8348417778298305), (5, 3, 0.9019529253178337), (5, 4, 0.9962321807552629), (5, 5, 0.9631815764127009);
DROP TABLE IF EXISTS R8;
CREATE TEMPORARY TABLE R8 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R8 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.8783226493995081), (1, 2, 0.960990368488509), (2, 0, 1.0), (2, 1, 1.034096699932827), (2, 2, 1.0468960340198719);
DROP TABLE IF EXISTS R9;
CREATE TEMPORARY TABLE R9 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R9 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.833642206455183), (1, 2, 0.8797782097592306), (2, 0, 1.0), (2, 1, 1.280716218540681), (2, 2, 0.8766326737204249);
DROP TABLE IF EXISTS R10;
CREATE TEMPORARY TABLE R10 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R10 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (0, 6, 1.0), (1, 0, 1.0), (1, 1, 0.9771721250042753), (1, 2, 0.9903765822017476), (1, 3, 0.9477023963292751), (1, 4, 1.0305045252353489), (1, 5, 0.8879003665212527), (1, 6, 0.9062306186879422), (2, 0, 1.0), (2, 1, 0.9834961384889508), (2, 2, 0.9926403924878939), (2, 3, 0.9601124029781256), (2, 4, 0.9755133075961777), (2, 5, 0.9333254604382527), (2, 6, 0.9283176196023614), (3, 0, 1.0), (3, 1, 1.0181235539921074), (3, 2, 0.9730137361130136), (3, 3, 0.9673102495094622), (3, 4, 1.0034720902405825), (3, 5, 1.2361483978333825), (3, 6, 0.8531808299468668), (4, 0, 1.0), (4, 1, 0.926354063556849), (4, 2, 1.020858917226419), (4, 3, 0.9244244895328791), (4, 4, 0.9102839855667587), (4, 5, 1.220887143641198), (4, 6, 1.4507762207136492), (5, 0, 1.0), (5, 1, 0.9777447244349138), (5, 2, 0.9507649910490437), (5, 3, 1.0139124998378657), (5, 4, 0.9568472004011815), (5, 5, 1.322712585709848), (5, 6, 1.1805013605751642), (6, 0, 1.0), (6, 1, 0.9560913033104171), (6, 2, 0.9409162281405197), (6, 3, 1.215290784055494), (6, 4, 1.1188767643188944), (6, 5, 1.1695241607585165), (6, 6, 1.2333556461078845), (7, 0, 1.0), (7, 1, 1.0763432252621932), (7, 2, 0.974470044215624), (7, 3, 0.9623775291891941), (7, 4, 1.1320221097485617), (7, 5, 0.9655508850588012), (7, 6, 0.8554633448599246), (8, 0, 1.0), (8, 1, 1.0155370069392564), (8, 2, 0.9753822953526277), (8, 3, 1.0258859530750162), (8, 4, 0.940244516665276), (8, 5, 0.940323762793364), (8, 6, 1.1241912881112641), (9, 0, 1.0), (9, 1, 0.9838493450412187), (9, 2, 0.9932023000054947), (9, 3, 1.0214107718118846), (9, 4, 0.9767330015281613), (9, 5, 0.7909554248360933), (9, 6, 0.9278306774446426), (10, 0, 1.0), (10, 1, 0.9864983765646224), (10, 2, 0.9952338672409936), (10, 3, 0.9642254768027364), (10, 4, 0.9786139051392799), (10, 5, 0.83950770053597), (10, 6, 0.934064102151445);
DROP TABLE IF EXISTS R11;
CREATE TEMPORARY TABLE R11 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R11 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 1.018186891569278), (1, 2, 0.918192929036965), (2, 0, 1.0), (2, 1, 0.9622053346096564), (2, 2, 0.9269749069367385), (3, 0, 1.0), (3, 1, 1.071636264682844), (3, 2, 0.937794806994044), (4, 0, 1.0), (4, 1, 1.2089546356857543), (4, 2, 1.0135475534817047), (5, 0, 1.0), (5, 1, 1.15211351370264), (5, 2, 1.095423037953773), (6, 0, 1.0), (6, 1, 1.034377078653479), (6, 2, 1.2861646324377591), (7, 0, 1.0), (7, 1, 0.9608574954532509), (7, 2, 1.1150298353989725), (8, 0, 1.0), (8, 1, 0.9919796426673343), (8, 2, 1.0318454485396111), (9, 0, 1.0), (9, 1, 0.9195530474412759), (9, 2, 0.9489675201406635), (10, 0, 1.0), (10, 1, 0.9365461318302506), (10, 2, 0.9168249966169446);
DROP TABLE IF EXISTS R12;
CREATE TEMPORARY TABLE R12 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R12 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (1, 0, 1.0), (1, 1, 0.901492281054814), (1, 2, 0.9048225621437166), (1, 3, 0.9678120324611169), (1, 4, 0.8973668413400429), (1, 5, 0.9427941921195617), (2, 0, 1.0), (2, 1, 1.393301239713371), (2, 2, 0.7741232061342049), (2, 3, 0.7263991527807834), (2, 4, 1.0636139778305156), (2, 5, 0.8621194719789897), (3, 0, 1.0), (3, 1, 1.0356890267942802), (3, 2, 1.3906519514912135), (3, 3, 0.9780756675516762), (3, 4, 1.0429464414285505), (3, 5, 0.8368299682699737), (4, 0, 1.0), (4, 1, 1.0491810579460263), (4, 2, 1.3686945683793734), (4, 3, 1.4534490515295608), (4, 4, 0.9584627948146246), (4, 5, 0.9472836761708842), (5, 0, 1.0), (5, 1, 0.8789960611831015), (5, 2, 1.451248899661243), (5, 3, 1.2255297317331075), (5, 4, 1.348101303223467), (5, 5, 0.9941033108048899), (6, 0, 1.0), (6, 1, 1.011196585627623), (6, 2, 1.224090500905972), (6, 3, 1.4123755964675446), (6, 4, 1.0725082818058107), (6, 5, 1.422482533401492), (7, 0, 1.0), (7, 1, 0.8539877714097555), (7, 2, 1.1849808626197484), (7, 3, 0.9959704902277555), (7, 4, 0.8440102250809814), (7, 5, 1.120685794839089), (8, 0, 1.0), (8, 1, 0.8438173443468907), (8, 2, 1.1572868408321284), (8, 3, 1.1715578734875216), (8, 4, 0.8445317211636119), (8, 5, 1.1075467108355042), (9, 0, 1.0), (9, 1, 1.0196551487114227), (9, 2, 0.832002859879176), (9, 3, 0.7801847923329526), (9, 4, 0.9191304226853246), (9, 5, 0.9847142883844613), (10, 0, 1.0), (10, 1, 1.0088851664781933), (10, 2, 0.8150163484090797), (10, 3, 0.7689978897708434), (10, 4, 1.0011337686989887), (10, 5, 0.9768357809871503);
DROP TABLE IF EXISTS R13;
CREATE TEMPORARY TABLE R13 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R13 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.6933771942360901), (1, 2, 1.177929331639569), (2, 0, 1.0), (2, 1, 0.659492396231282), (2, 2, 0.7911564208123909), (3, 0, 1.0), (3, 1, 0.8076548326617525), (3, 2, 1.9909193055300585), (4, 0, 1.0), (4, 1, 0.641739893990595), (4, 2, 1.0739366015097835), (5, 0, 1.0), (5, 1, 17.347522397994002), (5, 2, 0.898747255333266), (6, 0, 1.0), (6, 1, 1.671373592341603), (6, 2, 1.8336757124830187);
DROP TABLE IF EXISTS R14;
CREATE TEMPORARY TABLE R14 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R14 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 0.9917224257519085), (1, 2, 1.0065861603182633), (2, 0, 1.0), (2, 1, 0.993410242678563), (2, 2, 0.9975317442976926), (3, 0, 1.0), (3, 1, 1.0013575595275273), (3, 2, 1.0098437720912719), (4, 0, 1.0), (4, 1, 0.9997487725152899), (4, 2, 1.002605702996172), (5, 0, 1.0), (5, 1, 1.0319920172920414), (5, 2, 0.9767739826320301), (6, 0, 1.0), (6, 1, 1.0237914836921902), (6, 2, 1.0023568346890304);
DROP TABLE IF EXISTS R15;
CREATE TEMPORARY TABLE R15 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R15 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (1, 0, 1.0), (1, 1, 0.9711925790316535), (1, 2, 1.0178586397324736), (1, 3, 0.9783756405520816), (1, 4, 0.9599787034168756), (1, 5, 0.9884156755885136), (2, 0, 1.0), (2, 1, 0.9841615603075708), (2, 2, 0.9742125630764), (2, 3, 0.936379382887144), (2, 4, 0.9789658492511931), (2, 5, 0.9722017195998441), (3, 0, 1.0), (3, 1, 0.9762516116021043), (3, 2, 1.069052551860672), (3, 3, 0.96440703271669), (3, 4, 1.0510179315291088), (3, 5, 0.9719485542448892), (4, 0, 1.0), (4, 1, 0.9578687979436735), (4, 2, 0.9980074592083334), (4, 3, 1.0865077047714766), (4, 4, 0.9916099420466642), (4, 5, 0.9699086961713234), (5, 0, 1.0), (5, 1, 1.0551058149373604), (5, 2, 1.4618004132711764), (5, 3, 1.393353983445842), (5, 4, 1.0346206174408135), (5, 5, 1.073427875246011), (6, 0, 1.0), (6, 1, 0.9733675564290883), (6, 2, 1.3071840066658793), (6, 3, 1.0846746728097318), (6, 4, 0.8743169690029697), (6, 5, 1.0218023734184671);
DROP TABLE IF EXISTS R16;
CREATE TEMPORARY TABLE R16 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R16 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (1, 0, 1.0), (1, 1, 0.8813667522687055), (2, 0, 1.0), (2, 1, 0.959220824597439), (3, 0, 1.0), (3, 1, 1.0287509884362993), (4, 0, 1.0), (4, 1, 1.0911906881058488), (5, 0, 1.0), (5, 1, 0.5395920669724991), (6, 0, 1.0), (6, 1, 1.0887307252490381);
DROP TABLE IF EXISTS R17;
CREATE TEMPORARY TABLE R17 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R17 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (1, 0, 1.0), (1, 1, 1.1620240447727794), (1, 2, 0.9304096007541602), (2, 0, 1.0), (2, 1, 1.1271251373844478), (2, 2, 1.1697711216036337);
DROP TABLE IF EXISTS R18;
CREATE TEMPORARY TABLE R18 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R18 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (1, 0, 1.0), (1, 1, 0.9936045046753473), (1, 2, 1.4123873525421589), (1, 3, 1.2424912643425268), (1, 4, 0.9857728000178977), (1, 5, 0.9831795913334882), (2, 0, 1.0), (2, 1, 0.9701524867364576), (2, 2, 1.1343642605947781), (2, 3, 1.0873512613870544), (2, 4, 0.9966712227755037), (2, 5, 1.0552865085764638);
DROP TABLE IF EXISTS R19;
CREATE TEMPORARY TABLE R19 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R19 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (1, 0, 1.0), (1, 1, 0.6360233537377433), (2, 0, 1.0), (2, 1, 1.0838349604759572);
DROP TABLE IF EXISTS R20;
CREATE TEMPORARY TABLE R20 (i INTEGER, j INTEGER, val DOUBLE PRECISION );
INSERT INTO R20 (i, j, val) VALUES (0, 0, 1.0), (0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0), (0, 4, 1.0), (0, 5, 1.0), (1, 0, 1.0), (1, 1, 0.9608324706086281), (1, 2, 0.7048052801321091), (1, 3, 1.4913075779558738), (1, 4, 0.8255098322035294), (1, 5, 1.2998779864025767);
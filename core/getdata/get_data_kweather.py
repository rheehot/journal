import urllib.request
import json
import csv

# list_url = "http://kweather.co.kr/air/data/code_data/bcode_arealist.json"
# with urllib.request.urlopen(list_url) as response:
#     dc = json.loads(response.read().decode("utf-8"))
#
# list_district = {}
# list_district_keys = []
# big_district = dc['11']['data']
# keylist = list(dc['11']['data'].keys())
# # print(keylist)
# for x in keylist:
#     for y in dc['11']['data'][x]['data']:
#         list_district[y] = dc['11']['data'][x]['data'][y]
#         list_district_keys.append(y)
# # print(big_district)
#
#
# district_url = "http://kweather.co.kr/air/data/area_realtime/MAP_PAST.php?code="
text = """강남구	개포동	46	#72da00	37.479097	127.059556
강남구	논현동	63	#72da00	37.508789	127.030511
강남구	대치동	66	#72da00	37.490506	127.063856
강남구	도곡동	49	#72da00	37.488067	127.040497
강남구	삼성동	73	#72da00	37.509042	127.057531
강남구	세곡동	52	#72da00	37.466367	127.109364
강남구	수서동	51	#72da00	37.480533	127.0886
강남구	신사동	77	#72da00	37.521339	127.025022
강남구	압구정동	77	#72da00	37.521339	127.025022
강남구	역삼동	77	#72da00	37.492583	127.035144
강남구	율현동	52	#72da00	37.466367	127.109364
강남구	일원동	44	#72da00	37.485175	127.075742
강남구	자곡동	52	#72da00	37.466367	127.109364
강남구	청담동	74	#72da00	37.525108	127.0493
강동구	강일동	71	#72da00	37.566714	127.1804
강동구	고덕동	70	#72da00	37.556244	127.151019
강동구	길동	51	#72da00	37.539217	127.146168
강동구	둔촌동	51	#72da00	37.52075	127.138831
강동구	명일동	56	#72da00	37.546964	127.148022
강동구	상일동	91	#ffbd00	37.566714	127.1804
강동구	성내동	63	#72da00	37.527847	127.126031
강동구	암사동	66	#72da00	37.548717	127.134764
강동구	천호동	107	#ffbd00	37.542303	127.138878	
강북구	미아동	46	#72da00	37.624483	127.020511
강북구	번동	52	#72da00	37.635158	127.031019
강북구	수유동	39	#72da00	37.630733	127.019297
강북구	우이동	51	#72da00	37.645194	127.014067		
강서구	가양동	131	#ff5a00	37.551044	126.873044
강서구	개화동	138	#ff5a00	37.563875	126.808831
강서구	공항동	125	#ff5a00	37.556106	126.812164
강서구	과해동	120	#ff5a00	37.556106	126.812164
강서구	내발산동	191	#ff5a00	37.550269	126.835244
강서구	등촌동	160	#ff5a00	37.553067	126.860997
강서구	마곡동	155	#ff5a00	37.566478	126.842664
강서구	방화동	132	#ff5a00	37.556106	126.812164
강서구	염창동	163	#ff5a00	37.551044	126.873044
강서구	오곡동	120	#ff5a00	37.556106	126.812164
강서구	오쇠동	120	#ff5a00	37.556106	126.812164
강서구	외발산동	216	#ff0000	37.550269	126.835244
강서구	화곡동	124	#ff5a00	37.527744	126.843742	
관악구	남현동	76	#72da00	37.471789	126.979956
관악구	봉천동	88	#ffbd00	37.485306	126.934886
관악구	신림동	80	#ffbd00	37.479735	126.9313	
광진구	광장동	65	#72da00	37.544214	127.105308
광진구	구의동	58	#72da00	37.539675	127.087867
광진구	군자동	36	#72da00	37.552353	127.077997
광진구	능동	44	#72da00	37.551028	127.082644
광진구	자양동	53	#72da00	37.531686	127.084419
광진구	중곡동	48	#72da00	37.557842	127.082164
광진구	화양동	53	#72da00	37.543786	127.073464
구로구	가리봉동	51	#72da00	37.477981	126.891986
구로구	개봉동	53	#72da00	37.499386	126.849264
구로구	고척동	66	#72da00	37.497608	126.8648
구로구	구로동	61	#72da00	37.490203	126.877856
구로구	궁동	58	#72da00	37.491106	126.833567
구로구	신도림동	63	#72da00	37.504978	126.882653
구로구	오류동	58	#72da00	37.494247	126.847089
구로구	온수동	58	#72da00	37.491106	126.833567
구로구	천왕동	53	#72da00	37.485992	126.841608
구로구	항동	53	#72da00	37.485992	126.841608	
금천구	가산동	69	#72da00	37.474125	126.893808
금천구	독산동	70	#72da00	37.467458	126.8991
금천구	시흥동	46	#72da00	37.452147	126.899419	
노원구	공릉동	39	#72da00	37.624727	127.073752
노원구	상계동	42	#72da00	37.655967	127.080089
노원구	월계동	41	#72da00	37.617319	127.065089
노원구	중계동	55	#72da00	37.645072	127.082456
노원구	하계동	41	#72da00	37.637783	127.074731
도봉구	도봉동	43	#72da00	37.675819	127.045511
도봉구	방학동	33	#72da00	37.661433	127.042767
도봉구	쌍문동	34	#72da00	37.645247	127.028178
도봉구	창동	52	#72da00	37.645647	127.045997
동대문구	답십리동	57	#72da00	37.569275	127.054222
동대문구	신설동	35	#72da00	37.575818	127.037217
동대문구	용두동	35	#72da00	37.575818	127.037217
동대문구	이문동	47	#72da00	37.595	127.067631
동대문구	장안동	59	#72da00	37.564986	127.068478
동대문구	전농동	48	#72da00	37.575211	127.049867
동대문구	제기동	46	#72da00	37.583077	127.037784
동대문구	청량리동	44	#72da00	37.586259	127.047277
동대문구	회기동	47	#72da00	37.588008	127.057489
동대문구	휘경동	45	#72da00	37.590158	127.067819
동작구	노량진동	65	#72da00	37.509481	126.944086
동작구	대방동	78	#72da00	37.505331	126.928444
동작구	동작동	39	#72da00	37.485619	126.979508
동작구	본동	58	#72da00	37.509481	126.944086
동작구	사당동	68	#72da00	37.473611	126.975733
동작구	상도1동	60	#72da00	37.50405	126.953022
동작구	상도동	65	#72da00	37.50405	126.953022
동작구	신대방동	94	#ffbd00	37.48615	126.912108
동작구	흑석동	58	#72da00	37.506739	126.962611
마포구	공덕동	48	#72da00	37.544344	126.954222
마포구	구수동	53	#72da00	37.544067	126.936642
마포구	노고산동	62	#72da00	37.55305	126.944811
마포구	당인동	57	#72da00	37.544447	126.934156
마포구	대흥동	52	#72da00	37.539247	126.943733
마포구	도화동	53	#72da00	37.547442	126.962089
마포구	동교동	71	#72da00	37.549656	126.922975
마포구	마포동	53	#72da00	37.5349	126.952131
마포구	망원동	65	#72da00	37.552433	126.907767
마포구	상수동	57	#72da00	37.544447	126.934156
마포구	상암동	58	#72da00	37.575514	126.896811
마포구	서교동	71	#72da00	37.549656	126.922975
마포구	성산동	77	#72da00	37.560583	126.910022
마포구	신공덕동	52	#72da00	37.547442	126.962089
마포구	신수동	54	#72da00	37.55305	126.944811
마포구	신정동	55	#72da00	37.544067	126.936642
마포구	아현동	49	#72da00	37.544344	126.954222
마포구	연남동	72	#72da00	37.561694	126.924067
마포구	염리동	48	#72da00	37.544344	126.954222
마포구	용강동	50	#72da00	37.539247	126.943733
마포구	중동	87	#ffbd00	37.565931	126.911153
마포구	창전동	57	#72da00	37.544447	126.934156
마포구	토정동	50	#72da00	37.539247	126.943733
마포구	하중동	57	#72da00	37.544447	126.934156
마포구	합정동	65	#72da00	37.546722	126.907753
마포구	현석동	53	#72da00	37.544067	126.936642	
서대문구	남가좌동	83	#ffbd00	37.571194	126.915578
서대문구	냉천동	45	#72da00	37.568303	126.961175
서대문구	대신동	59	#72da00	37.556739	126.945586
서대문구	대현동	55	#72da00	37.556869	126.958911
서대문구	미근동	50	#72da00	37.562061	126.956844
서대문구	봉원동	59	#72da00	37.556739	126.945586
서대문구	북가좌동	47	#72da00	37.576711	126.908978
서대문구	북아현동	51	#72da00	37.556869	126.958911
서대문구	신촌동	59	#72da00	37.556739	126.945586
서대문구	연희동	48	#72da00	37.571122	126.937353
서대문구	영천동	45	#72da00	37.568303	126.961175
서대문구	옥천동	45	#72da00	37.568303	126.961175
서대문구	창천동	59	#72da00	37.556739	126.945586
서대문구	천연동	45	#72da00	37.568303	126.961175
서대문구	충정로2가	50	#72da00	37.562061	126.956844
서대문구	충정로3가	50	#72da00	37.562061	126.956844
서대문구	합동	50	#72da00	37.562061	126.956844
서대문구	현저동	45	#72da00	37.568303	126.961175
서대문구	홍은동	38	#72da00	37.590431	126.945956
서대문구	홍제동	48	#72da00	37.5849	126.946986	
서초구	내곡동	42	#72da00	37.459144	127.053411
서초구	반포동	47	#72da00	37.49765	126.988133
서초구	방배동	59	#72da00	37.480783	127.014567
서초구	서초동	42	#72da00	37.486	127.021111
서초구	신원동	42	#72da00	37.459144	127.053411
서초구	양재동	49	#72da00	37.481636	127.038153
서초구	염곡동	42	#72da00	37.459144	127.053411
서초구	우면동	51	#72da00	37.481636	127.038153
서초구	원지동	46	#72da00	37.467781	127.043144
서초구	잠원동	45	#72da00	37.512089	127.016053
성동구	금호동1가	71	#72da00	37.552069	127.023944
성동구	금호동2가	66	#72da00	37.553188	127.020859
성동구	금호동3가	66	#72da00	37.553188	127.020859
성동구	금호동4가	64	#72da00	37.544472	127.024475
성동구	도선동	65	#72da00	37.567754	127.025559
성동구	마장동	50	#72da00	37.563433	127.047564
성동구	사근동	60	#72da00	37.558406	127.047956
성동구	상왕십리동	65	#72da00	37.567754	127.025559
성동구	성수동1가	55	#72da00	37.538958	127.051986
성동구	성수동2가	61	#72da00	37.536703	127.0562
성동구	송정동	68	#72da00	37.551728	127.071708
성동구	옥수동	52	#72da00	37.543717	127.013463
성동구	용답동	66	#72da00	37.561367	127.057433
성동구	응봉동	79	#72da00	37.550347	127.035497
성동구	하왕십리동	132	#ff5a00	37.558336	127.032711
성동구	행당동	102	#ffbd00	37.558406	127.047956
성동구	홍익동	65	#72da00	37.567754	127.025559
성북구	길음동	43	#72da00	37.601783	127.024167
성북구	돈암동	50	#72da00	37.582847	127.009556
성북구	동선동1가	53	#72da00	37.591278	127.022508
성북구	동선동2가	53	#72da00	37.591278	127.022508
성북구	동선동3가	53	#72da00	37.591278	127.022508
성북구	동선동4가	53	#72da00	37.591278	127.022508
성북구	동선동5가	53	#72da00	37.591278	127.022508
성북구	동소문동1가	46	#72da00	37.587442	127.006086
성북구	동소문동2가	55	#72da00	37.582847	127.009556
성북구	동소문동3가	55	#72da00	37.582847	127.009556
성북구	동소문동4가	46	#72da00	37.587442	127.006086
성북구	동소문동5가	55	#72da00	37.582847	127.009556
성북구	동소문동6가	53	#72da00	37.591278	127.022508
성북구	동소문동7가	53	#72da00	37.591278	127.022508
성북구	보문동1가	45	#72da00	37.577589	127.0249
성북구	보문동2가	45	#72da00	37.577589	127.0249
성북구	보문동3가	45	#72da00	37.577589	127.0249
성북구	보문동4가	45	#72da00	37.577589	127.0249
성북구	보문동5가	45	#72da00	37.577589	127.0249
성북구	보문동6가	45	#72da00	37.577589	127.0249
성북구	보문동7가	45	#72da00	37.577589	127.0249
성북구	삼선동1가	55	#72da00	37.582847	127.009556
성북구	삼선동2가	55	#72da00	37.582847	127.009556
성북구	삼선동3가	55	#72da00	37.582847	127.009556
성북구	삼선동4가	55	#72da00	37.582847	127.009556
성북구	삼선동5가	55	#72da00	37.582847	127.009556
성북구	상월곡동	43	#72da00	37.599942	127.041689
성북구	석관동	44	#72da00	37.610161	127.063519
성북구	성북동	46	#72da00	37.587442	127.006086
성북구	성북동1가	46	#72da00	37.587442	127.006086
성북구	안암동1가	57	#72da00	37.583058	127.023478
성북구	안암동2가	57	#72da00	37.583058	127.023478
성북구	안암동3가	57	#72da00	37.583058	127.023478
성북구	안암동4가	57	#72da00	37.583058	127.023478
성북구	안암동5가	57	#72da00	37.583058	127.023478
성북구	장위동	45	#72da00	37.611192	127.045856
성북구	정릉동	46	#72da00	37.598642	127.018742
성북구	종암동	47	#72da00	37.597331	127.033553
성북구	하월곡동	47	#72da00	37.60385	127.0294		
송파구	가락동	49	#72da00	37.492772	127.123911
송파구	거여동	53	#72da00	37.494108	127.145408
송파구	마천동	56	#72da00	37.493222	127.152089
송파구	문정동	48	#72da00	37.487192	127.1262
송파구	방이동	63	#72da00	37.508147	127.126011
송파구	삼전동	47	#72da00	37.499978	127.094642
송파구	석촌동	58	#72da00	37.500775	127.105753
송파구	송파동	45	#72da00	37.503131	127.111819
송파구	신천동	95	#ffbd00	37.516444	127.110056
송파구	오금동	50	#72da00	37.50015	127.130244
송파구	잠실동	54	#72da00	37.503356	127.086419
송파구	장지동	50	#72da00	37.487053	127.113064
송파구	풍납동	76	#72da00	37.535247	127.124244	
양천구	목동	106	#ffbd00	37.527539	126.873233
양천구	신월동	89	#ffbd00	37.530006	126.8336
양천구	신정동	66	#72da00	37.515731	126.856397		
영등포구	당산동	73	#72da00	37.531939	126.904244
영등포구	당산동1가	68	#72da00	37.522158	126.899522
영등포구	당산동2가	68	#72da00	37.522158	126.899522
영등포구	당산동3가	68	#72da00	37.522158	126.899522
영등포구	당산동4가	73	#72da00	37.531939	126.904244
영등포구	당산동5가	73	#72da00	37.531939	126.904244
영등포구	당산동6가	73	#72da00	37.531939	126.904244
영등포구	대림동	68	#72da00	37.498822	126.907344
영등포구	도림동	71	#72da00	37.509475	126.89595
영등포구	문래동1가	67	#72da00	37.517097	126.899542
영등포구	문래동2가	67	#72da00	37.517097	126.899542
영등포구	문래동3가	67	#72da00	37.517097	126.899542
영등포구	문래동4가	67	#72da00	37.517097	126.899542
영등포구	문래동5가	67	#72da00	37.517097	126.899542
영등포구	문래동6가	67	#72da00	37.517097	126.899542
영등포구	신길동	74	#72da00	37.514683	126.909305
영등포구	양평동	72	#72da00	37.535	126.898022
영등포구	양평동1가	73	#72da00	37.520847	126.890286
영등포구	양평동2가	73	#72da00	37.520847	126.890286
영등포구	양평동3가	72	#72da00	37.520847	126.890286
영등포구	양평동4가	72	#72da00	37.535	126.898022
영등포구	양평동5가	72	#72da00	37.535	126.898022
영등포구	양평동6가	72	#72da00	37.535	126.898022
영등포구	양화동	72	#72da00	37.535	126.898022
영등포구	여의도동	91	#ffbd00	37.514889	126.936756
영등포구	영등포동	100	#ffbd00	37.514683	126.909305
영등포구	영등포동1가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동2가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동3가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동4가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동5가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동6가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동7가	120	#ff5a00	37.520398	126.910691
영등포구	영등포동8가	120	#ff5a00	37.520398	126.910691	
용산구	갈월동	47	#72da00	37.542833	126.976967
용산구	남영동	47	#72da00	37.542833	126.976967
용산구	도원동	71	#72da00	37.53625	126.959664
용산구	동빙고동	50	#72da00	37.517606	126.996778
용산구	동자동	47	#72da00	37.542833	126.976967
용산구	문배동	54	#72da00	37.535869	126.968342
용산구	보광동	54	#72da00	37.523464	127.002333
용산구	산천동	57	#72da00	37.531592	126.953578
용산구	서계동	44	#72da00	37.542556	126.972042
용산구	서빙고동	50	#72da00	37.517606	126.996778
용산구	신계동	54	#72da00	37.535869	126.968342
용산구	신창동	57	#72da00	37.531592	126.953578
용산구	용문동	71	#72da00	37.53625	126.959664
용산구	용산동1가	47	#72da00	37.542833	126.976967
용산구	용산동2가	48	#72da00	37.543119	126.987564
용산구	용산동3가	55	#72da00	37.526242	126.971533
용산구	용산동4가	48	#72da00	37.543119	126.987564
용산구	용산동5가	55	#72da00	37.526242	126.971533
용산구	용산동6가	50	#72da00	37.517606	126.996778
용산구	원효로1가	54	#72da00	37.535869	126.968342
용산구	원효로2가	54	#72da00	37.535869	126.968342
용산구	원효로3가	57	#72da00	37.531592	126.953578
용산구	원효로4가	57	#72da00	37.531592	126.953578
용산구	이촌동	58	#72da00	37.518403	126.975356
용산구	이태원동	52	#72da00	37.529492	126.997042
용산구	주성동	50	#72da00	37.517606	126.996778
용산구	청암동	57	#72da00	37.531592	126.953578
용산구	청파동1가	44	#72da00	37.542556	126.972042
용산구	청파동2가	44	#72da00	37.542556	126.972042
용산구	청파동3가	44	#72da00	37.542556	126.972042
용산구	한강로1가	55	#72da00	37.526242	126.971533
용산구	한강로2가	55	#72da00	37.526242	126.971533
용산구	한강로3가	55	#72da00	37.526242	126.971533
용산구	한남동	51	#72da00	37.531886	127.002644
용산구	효창동	59	#72da00	37.538953	126.963397
용산구	후암동	47	#72da00	37.545881	126.980267	
은평구	갈현동	42	#72da00	37.620897	126.918789
은평구	구산동	41	#72da00	37.609019	126.9125
은평구	녹번동	41	#72da00	37.599961	126.936844
은평구	대조동	43	#72da00	37.611339	126.922889
은평구	불광동	38	#72da00	37.607536	126.934189
은평구	수색동	48	#72da00	37.581358	126.899642
은평구	신사동	50	#72da00	37.595219	126.914386
은평구	역촌동	47	#72da00	37.601619	126.917278
은평구	응암동	45	#72da00	37.597911	126.928864
은평구	증산동	44	#72da00	37.581531	126.909222
은평구	진관동	48	#72da00	37.6356	126.921111	
종로구	가회동	58	#72da00	37.577253	126.986911
종로구	견지동	56	#72da00	37.567886	126.991067
종로구	경운동	56	#72da00	37.567886	126.991067
종로구	계동	58	#72da00	37.577253	126.986911
종로구	공평동	56	#72da00	37.567886	126.991067
종로구	관수동	56	#72da00	37.567886	126.991067
종로구	관철동	56	#72da00	37.567886	126.991067
종로구	관훈동	56	#72da00	37.567886	126.991067
종로구	교남동	42	#72da00	37.569075	126.9641
종로구	교북동	42	#72da00	37.569075	126.9641
종로구	구기동	54	#72da00	37.602522	126.968878
종로구	궁정동	48	#72da00	37.584137	126.970652
종로구	권농동	56	#72da00	37.567886	126.991067
종로구	낙원동	56	#72da00	37.567886	126.991067
종로구	내수동	46	#72da00	37.573269	126.970956
종로구	내자동	46	#72da00	37.573269	126.970956
종로구	누상동	48	#72da00	37.584137	126.970652
종로구	누하동	48	#72da00	37.584137	126.970652
종로구	당주동	46	#72da00	37.573269	126.970956
종로구	도렴동	46	#72da00	37.573269	126.970956
종로구	돈의동	56	#72da00	37.567886	126.991067
종로구	동숭동	49	#72da00	37.574214	127.006397
종로구	명륜1가	53	#72da00	37.583989	127.002622
종로구	명륜2가	53	#72da00	37.583989	127.002622
종로구	명륜3가	53	#72da00	37.583989	127.002622
종로구	명륜4가	53	#72da00	37.583989	127.002622
종로구	묘동	56	#72da00	37.567886	126.991067
종로구	무악동	47	#72da00	37.571539	126.961208
종로구	봉익동	56	#72da00	37.567886	126.991067
종로구	부암동	49	#72da00	37.589856	126.966444
종로구	사간동	44	#72da00	37.582425	126.983978
종로구	사직동	46	#72da00	37.573269	126.970956
종로구	삼청동	44	#72da00	37.582425	126.983978
종로구	서린동	56	#72da00	37.567886	126.991067
종로구	세종로	50	#72da00	37.584137	126.970652
종로구	소격동	44	#72da00	37.582425	126.983978
종로구	송월동	42	#72da00	37.569075	126.9641
종로구	송현동	44	#72da00	37.582425	126.983978
종로구	수송동	56	#72da00	37.567886	126.991067
종로구	숭인동	58	#72da00	37.575028	127.017664
종로구	신교동	48	#72da00	37.584137	126.970652
종로구	신문로1가	46	#72da00	37.573269	126.970956
종로구	신문로2가	46	#72da00	37.573269	126.970956
종로구	신영동	49	#72da00	37.589856	126.966444
종로구	안국동	44	#72da00	37.582425	126.983978
종로구	연건동	49	#72da00	37.574214	127.006397
종로구	연지동	47	#72da00	37.569211	127.007156
종로구	예지동	56	#72da00	37.567886	126.991067
종로구	옥인동	48	#72da00	37.584137	126.970652
종로구	와룡동	54	#72da00	37.567886	126.991067
종로구	운니동	56	#72da00	37.567886	126.991067
종로구	원남동	56	#72da00	37.567886	126.991067
종로구	원서동	58	#72da00	37.577253	126.986911
종로구	이화동	49	#72da00	37.574214	127.006397
종로구	익선동	56	#72da00	37.567886	126.991067
종로구	인사동	56	#72da00	37.567886	126.991067
종로구	인의동	56	#72da00	37.567886	126.991067
종로구	장사동	56	#72da00	37.567886	126.991067
종로구	재동	58	#72da00	37.577253	126.986911
종로구	적선동	46	#72da00	37.573269	126.970956
종로구	종로1가	56	#72da00	37.567886	126.991067
종로구	종로2가	56	#72da00	37.567886	126.991067
종로구	종로3가	56	#72da00	37.567886	126.991067
종로구	종로4가	56	#72da00	37.567886	126.991067
종로구	종로5가	47	#72da00	37.569211	127.007156
종로구	종로6가	47	#72da00	37.569211	127.007156
종로구	중학동	56	#72da00	37.567886	126.991067
종로구	창성동	48	#72da00	37.584137	126.970652
종로구	창신동	54	#72da00	37.567936	127.018464
종로구	청운동	48	#72da00	37.584137	126.970652
종로구	청진동	56	#72da00	37.567886	126.991067
종로구	체부동	46	#72da00	37.573269	126.970956
종로구	충신동	47	#72da00	37.569211	127.007156
종로구	통의동	46	#72da00	37.573269	126.970956
종로구	통인동	48	#72da00	37.584137	126.970652
종로구	팔판동	44	#72da00	37.582425	126.983978
종로구	평동	42	#72da00	37.569075	126.9641
종로구	평창동	54	#72da00	37.602522	126.968878
종로구	필운동	46	#72da00	37.573269	126.970956
종로구	행촌동	42	#72da00	37.569075	126.9641
종로구	혜화동	53	#72da00	37.583989	127.002622
종로구	홍지동	49	#72da00	37.589856	126.966444
종로구	홍파동	42	#72da00	37.569075	126.9641
종로구	화동	44	#72da00	37.582425	126.983978
종로구	효자동	48	#72da00	37.584137	126.970652
종로구	효제동	47	#72da00	37.569211	127.007156
종로구	훈정동	56	#72da00	37.567886	126.991067		
중구	광희동1가	52	#72da00	37.561731	127.007164
중구	광희동2가	52	#72da00	37.561731	127.007164
중구	남대문로1가	48	#72da00	37.557236	126.987889
중구	남대문로2가	48	#72da00	37.559631	126.979108
중구	남대문로3가	46	#72da00	37.559631	126.979108
중구	남대문로4가	46	#72da00	37.559631	126.979108
중구	남대문로5가	46	#72da00	37.554483	126.981444
중구	남산동1가	48	#72da00	37.557236	126.987889
중구	남산동2가	48	#72da00	37.557236	126.987889
중구	남산동3가	48	#72da00	37.557236	126.987889
중구	남창동	46	#72da00	37.554483	126.981444
중구	남학동	48	#72da00	37.557353	126.997711
중구	다동	48	#72da00	37.557236	126.987889
중구	만리동1가	52	#72da00	37.552033	126.9666
중구	만리동2가	52	#72da00	37.552033	126.9666
중구	명동1가	48	#72da00	37.557236	126.987889
중구	명동2가	48	#72da00	37.557236	126.987889
중구	무교동	48	#72da00	37.557236	126.987889
중구	무학동	60	#72da00	37.559311	127.016633
중구	묵정동	51	#72da00	37.557353	126.997711
중구	방산동	52	#72da00	37.5639	126.993431
중구	봉래동1가	46	#72da00	37.559631	126.979108
중구	봉래동2가	46	#72da00	37.554483	126.981444
중구	북창동	47	#72da00	37.559631	126.979108
중구	산림동	52	#72da00	37.5639	126.993431
중구	삼각동	48	#72da00	37.557236	126.987889
중구	서소문동	47	#72da00	37.559631	126.979108
중구	소공동	47	#72da00	37.559631	126.979108
중구	수표동	48	#72da00	37.557236	126.987889
중구	수하동	48	#72da00	37.557236	126.987889
중구	순화동	46	#72da00	37.559631	126.979108
중구	신당동	60	#72da00	37.559311	127.016633
중구	쌍림동	52	#72da00	37.561731	127.007164
중구	예관동	52	#72da00	37.561731	127.007164
중구	예장동	48	#72da00	37.557236	126.987889
중구	오장동	52	#72da00	37.561731	127.007164
중구	을지로1가	48	#72da00	37.557236	126.987889
중구	을지로2가	48	#72da00	37.557236	126.987889
중구	을지로3가	52	#72da00	37.5639	126.993431
중구	을지로4가	52	#72da00	37.5639	126.993431
중구	을지로5가	52	#72da00	37.5639	126.993431
중구	을지로6가	52	#72da00	37.561731	127.007164
중구	을지로7가	52	#72da00	37.561731	127.007164
중구	의주로1가	47	#72da00	37.559631	126.979108
중구	의주로2가	52	#72da00	37.552033	126.9666
중구	인현동1가	52	#72da00	37.5639	126.993431
중구	인현동2가	52	#72da00	37.561731	127.007164
중구	입정동	52	#72da00	37.5639	126.993431
중구	장교동	48	#72da00	37.557236	126.987889
중구	장충동1가	53	#72da00	37.559117	127.009933
중구	장충동2가	51	#72da00	37.557353	126.997711
중구	저동1가	48	#72da00	37.557236	126.987889
중구	저동2가	52	#72da00	37.5639	126.993431
중구	정동	47	#72da00	37.559631	126.979108
중구	주교동	52	#72da00	37.5639	126.993431
중구	주자동	48	#72da00	37.557353	126.997711
중구	중림동	52	#72da00	37.552033	126.9666
중구	초동	52	#72da00	37.5639	126.993431
중구	충무로1가	47	#72da00	37.554483	126.981444
중구	충무로2가	48	#72da00	37.557236	126.987889
중구	충무로3가	48	#72da00	37.557353	126.997711
중구	충무로4가	50	#72da00	37.557353	126.997711
중구	충무로5가	50	#72da00	37.557353	126.997711
중구	충정로1가	47	#72da00	37.559631	126.979108
중구	태평로1가	48	#72da00	37.557236	126.987889
중구	태평로2가	47	#72da00	37.559631	126.979108
중구	필동1가	48	#72da00	37.557353	126.997711
중구	필동2가	48	#72da00	37.557353	126.997711
중구	필동3가	48	#72da00	37.557353	126.997711
중구	황학동	59	#72da00	37.564664	127.023497
중구	회현동1가	47	#72da00	37.554483	126.981444
중구	회현동2가	47	#72da00	37.554483	126.981444
중구	회현동3가	48	#72da00	37.557236	126.987889
중구	흥인동	60	#72da00	37.559311	127.016633	
중랑구	망우동	84	#ffbd00	37.598692	127.108464
중랑구	면목동	42	#72da00	37.586983	127.081133
중랑구	묵동	35	#72da00	37.609622	127.080586
중랑구	상봉동	42	#72da00	37.597028	127.089289
중랑구	신내동	97	#ffbd00	37.603083	127.101553
중랑구	중화동	37	#72da00	37.598386	127.082778
"""
t=text.split('\n')


f = open('../kdata_mean.csv', 'w', encoding='utf-8')
wr = csv.writer(f)
wr.writerow(['gu','name','mean','color','lat','lon'])
for x in t:
    k = x.split('\t')
    wr.writerow(k)

# for x in keylist:
#     big_district_name = big_district[x]['name']
#     mean_big = 0
#     le = 0
#     for y in dc['11']['data'][x]['data']:
#         with urllib.request.urlopen(district_url + y) as response:
#             dc2 = json.loads(response.read().decode("utf-8"))
#             ls = dc2['data']
#         mean = 0
#         for z in ls:
#             mean += int(z.split("#")[1])
#         mean = int(mean / 24)
#         wr.writerow([big_district_name,list_district[y],mean])
#         mean_big += mean
#         le += 1
#     wr.writerow([big_district_name,'', mean_big/le])
#     print(big_district_name)

f.close()
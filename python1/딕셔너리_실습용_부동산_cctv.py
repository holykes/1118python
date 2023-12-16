###########################
'''
1. 아래 data, cctv 변수의 데이터를 보기좋게 정렬하기
2. data 변수에서 도로명과 거래금액 추출하기. 반복문 사용
3. cctv 변수에서 점포명만 추출하기. 반복문 사용

json 데이터를 정렬하는 사이트들
    https://tools.arantius.com/tabifier
    https://jsoneditoronline.org/
    https://jsonviewer.stack.hu/
    https://beautifytools.com/xml-viewer-editor.php
'''
###########################

data={'response': {'header': {'resultCode': '00', 'resultMsg': 'NORMAL SERVICE.'},
	'body': {'items': {'item': [{'거래금액': '82,500', '건축년도': '2008', '도로명': '세종대로23길'},
			  {'거래금액': '130,000', '건축년도': '2004', '도로명': '경희궁2길'}]},
	           'numOfRows': '10',
	           'pageNo': '1',
	           'totalCount': '49'}}
        }


cctv={'fields':
        [
            {'id':'점포명'},
            {'id':'소재지도로명주소'}
        ],
    'records':
        [
            {'점포명':'CU 도계사랑점','소재지도로명주소':'경상남도 창원시 의창구 원이대로81번길 28'},
            {'점포명':'세븐일레븐(소답점)','소재지도로명주소':'경상남도 창원시 의창구 의안로2번길 25'},
            {'점포명':'GS25 봉곡성우점','소재지도로명주소':'경상남도 창원시 의창구 지귀로 14'}
        ]
    }


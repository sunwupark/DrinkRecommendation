#라이브러리
import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm

#외국술 crawling (liquor)
liquor = pd.read_csv('liquor_data.csv')

##Main Ingredients 리스트화
liquor['Main Ingredients'].fillna('', inplace = True)
for i in range(len(liquor)):
    liquor['Main Ingredients'][i] = liquor['Main Ingredients'][i].split(', ')

#술담화 crawling (trad)
trad = pd.read_csv('술담화_final.csv')

#the sool crawling (trad1)
trad1 = pd.read_csv('the_sool_final.csv')
trad1['number'] = trad1['number'].astype(int)
trad1['Unnamed: 0'] = trad1['Unnamed: 0'].astype(int)

#나라 데이터 crawling (countries)
countries = pd.read_csv('Countries.csv')


#제조법 별 구분

##분류기준
fermented = ['탁주', '살균약주', '약주', '과실주', '청주', '약주, 청주', '살균탁주', 'Fermented']
distilled = ['증류주','리큐르', '증류식소주', '일반증류주', 'Distilled']
##liquor의 분류
fermented_liquor = []
distilled_liquor = []
else_liquor = []

for i in range(len(liquor)):
  if liquor.iloc[i][9] in fermented:
    fermented_liquor.append(liquor.iloc[i][1])
  elif liquor.iloc[i][9] in distilled:
    distilled_liquor.append(liquor.iloc[i][1])
  else:
    else_liquor.append(liquor.iloc[i][1])

##술담화의 분류
fermented_trad = []
distilled_trad = []
else_trad = []

for i in range(len(trad)):
  if trad.iloc[i][5] in fermented:
    fermented_trad.append(trad.iloc[i][0])
  elif trad.iloc[i][5] in distilled:
    distilled_trad.append(trad.iloc[i][0])
  else:
    else_trad.append(trad.iloc[i][0])

##the sool의 분류
fermented_trad1 = []
distilled_trad1 = []
else_trad1 = []

for i in range(len(trad1)):
  if trad1.iloc[i][4] == '리큐르/기타주류':
    if trad1.iloc[i][6] >= 18:
      distilled_trad1.append(trad1.iloc[i][0])
    else :
      else_trad1.append(trad1.iloc[i][0])
  elif trad1.iloc[i][4] in fermented:
    fermented_trad1.append(trad1.iloc[i][0])
  elif trad1.iloc[i][4] in distilled:
    distilled_trad1.append(trad1.iloc[i][0])
  else:
    else_trad1.append(trad1.iloc[i][0])

#재료 별 구분

##분류기준
gin = ['Gin', 'Juniper berry', '솔잎', '노간주나무 열매', '주니퍼 베리', '송순', '노간 나무 열매', '노간주']
grain = ['Vodka', 'Rum', 'Tequila', 'Malted barley', 'Barley', 'Grain', 'Wheat','Corn', 'Rye', 'Rice', '누룩', '쌀', '곡물', '통밀', '보리']
grain_etc = ['공주밤','고구마', '토란', 'Agave', 'Sugarcane', '사탕수수']
spices = ['Vermouth','Tabasco', 'Mint', 'Cola', 'Tonic', '허브', '땅콩', '단호박', '양파', '생강', '연잎', '모싯잎', '버섯', '홍삼', '커피', '잣', '인삼', '강황']
fruit = ['Tomato', 'Apple', '매실', '복숭아', '자두', '체리', '버찌', '딸기', '무화과', '사과', '애플', '배', '망고', '패션후르츠', '파인애플']
whiskey = ['Whiskey', 'Oak', '오크통', '오크']
citrus = ['Lime', 'Lemon', '유자', '감귤', '라임', '레몬']
grape = ['Red grape', 'Cranberry', 'White grape', '포도', '청포도', '라즈베리','모스카토', '거봉', '복분자','오디', '오미자', '구기자', '샤인머스켓', '산수유', '머루', '머스켓', '캠벨', '켐벨']
floral = ['Hops', 'Pale Malt', '동백꽃', '진달래 꽃', '유채꽃', '국화', '연꽃']

##liquor의 분류
gin_liquor = []
grain_liquor = []
grain_etc_liquor = []
spices_liquor = []
fruit_liquor = []
whiskey_liquor = []
citrus_liquor = []
grape_liquor = []
floral_liquor = []

for i in range(len(liquor)):
    for j in range(len(gin)):
        if gin[j] in liquor.iloc[i][8]:
            gin_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(grain)):
        if grain[j] in liquor.iloc[i][8]:
            grain_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(grain_etc)):
        if grain_etc[j] in liquor.iloc[i][8]:
            grain_etc_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(spices)):
        if spices[j] in liquor.iloc[i][8]:
            spices_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(fruit)):
        if fruit[j] in liquor.iloc[i][8]:
            fruit_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(whiskey)):
        if whiskey[j] in liquor.iloc[i][8]:
            whiskey_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(citrus)):
        if citrus[j] in liquor.iloc[i][8]:
            citrus_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(grape)):
        if grape[j] in liquor.iloc[i][8]:
            grape_liquor.append(liquor.iloc[i][1])
            break
    for j in range(len(floral)):
        if floral[j] in liquor.iloc[i][8]:
            floral_liquor.append(liquor.iloc[i][1])
            break

##술담화의 분류
trad['info'].fillna('', inplace = True)

gin_trad = []
grain_trad = []
grain_etc_trad = []
spices_trad = []
fruit_trad = []
whiskey_trad = []
citrus_trad = []
grape_trad = []
floral_trad = []


for i in range(len(trad)):
  for j in range(len(gin)):
    if gin[j] in trad.iloc[i][10]:
      gin_trad.append(trad.iloc[i][1])
      break
  for j in range(len(grain)):
    if grain[j] in trad.iloc[i][10]:
      grain_trad.append(trad.iloc[i][1])
      break
  for j in range(len(grain_etc)):
    if grain_etc[j] in trad.iloc[i][10]:
      grain_etc_trad.append(trad.iloc[i][1])
      break
  for j in range(len(spices)):
    if spices[j] in trad.iloc[i][10]:
      spices_trad.append(trad.iloc[i][1])
      break
  for j in range(len(fruit)):
    if fruit[j] in trad.iloc[i][10]:
      fruit_trad.append(trad.iloc[i][1])
      break
  for j in range(len(whiskey)):
    if whiskey[j] in trad.iloc[i][10]:
      whiskey_trad.append(trad.iloc[i][1])
      break
  for j in range(len(citrus)):
    if citrus[j] in trad.iloc[i][10]:
      citrus_trad.append(trad.iloc[i][1])
      break
  for j in range(len(grape)):
    if grape[j] in trad.iloc[i][10]:
      grape_trad.append(trad.iloc[i][1])
      break
  for j in range(len(floral)):
    if floral[j] in trad.iloc[i][10]:
      floral_trad.append(trad.iloc[i][1])
      break

##the sool의 분류
trad1['원재료'].fillna('', inplace=True)
trad1['제품 소개'].fillna('', inplace=True)

gin_trad1 = []
grain_trad1 = []
grain_etc_trad1 = []
spices_trad1 = []
fruit_trad1 = []
whiskey_trad1 = []
citrus_trad1 = []
grape_trad1 = []
floral_trad1 = []

for i in range(len(trad1)):
    for j in range(len(gin)):
        if gin[j] in trad1.iloc[i][5]:
            gin_trad1.append(trad1.iloc[i][0])
            break
    for j in range(len(grain)):
        if grain[j] in trad1.iloc[i][5]:
            grain_trad1.append(trad1.iloc[i][0])
            break
    for j in range(len(grain_etc)):
        if grain_etc[j] in trad1.iloc[i][5]:
            grain_etc_trad1.append(trad1.iloc[i][0])
            break
    for j in range(len(spices)):
        if spices[j] in trad1.iloc[i][5]:
            spices_trad1.append(trad1.iloc[i][0])
            break
    for j in range(len(fruit)):
        if fruit[j] in trad1.iloc[i][5]:
            fruit_trad1.append(trad1.iloc[i][0])
            break
            # 원재료가 아니라 제품 소개로 검색
    for j in range(len(whiskey)):
        if whiskey[j] in trad1.iloc[i][8]:
            whiskey_trad1.append(trad1.iloc[i][0])
            break
    for j in range(len(citrus)):
        if citrus[j] in trad1.iloc[i][5]:
            citrus_trad1.append(trad1.iloc[i][0])
            break
    for j in range(len(grape)):
        if grape[j] in trad1.iloc[i][5]:
            grape_trad1.append(trad1.iloc[i][0])
            break
    # 원재료가 아니라 제품 소개로 검색
    for j in range(len(floral)):
        if floral[j] in trad1.iloc[i][8]:
            floral_trad1.append(trad1.iloc[i][0])
            break

#맛 별 구분

##liquor의 맛 벡터
taste_liquor = liquor[['Bitter',	'Sweet',	'Sour', 'Spicy', 'Salty',	'Carbonated']]
taste_liquor_list = np.array(taste_liquor.values.tolist())

##술담화의 맛 벡터
taste_trad = trad[['bitter',	'sweet',	'sour',	'spicy', 'salty',	'sparkle']]
taste_trad_list = np.array(taste_trad.values.tolist())

##the sool의 맛 벡터
taste_trad1 = trad1[['bitter',	'sweet',	'sour',	'spicy', 'salty',	'sparkle']]
taste_trad1_list = np.array(taste_trad1.values.tolist())

#도수 별 구분

##사용자 선택 도수 데이터만 추출
#술담화

user_level1_damwha = []
user_level2_damwha = []
user_level3_damwha = []
user_level4_damwha = []
user_level5_damwha = []
user_level6_damwha = []

for i in range(len(trad)):
  if trad.loc[i]['도수'] <= 7:
    user_level1_damwha.append(i)
  elif 7 < trad.loc[i]['도수'] <= 12:
    user_level2_damwha.append(i)
  elif 12 < trad.loc[i]['도수'] <= 15:
    user_level3_damwha.append(i)
  elif 15 < trad.loc[i]['도수'] <= 25:
    user_level4_damwha.append(i)
  elif 25 < trad.loc[i]['도수'] <= 40:
    user_level5_damwha.append(i)
  else:
    user_level6_damwha.append(i)

#the_sool

user_level1_sool = []
user_level2_sool = []
user_level3_sool = []
user_level4_sool = []
user_level5_sool = []
user_level6_sool = []

for i in range(len(trad1)):
  if trad1.loc[i]['도수'] <= 7:
    user_level1_sool.append(i)
  elif 7 < trad1.loc[i]['도수'] <= 12:
    user_level2_sool.append(i)
  elif 12 < trad1.loc[i]['도수'] <= 15:
    user_level3_sool.append(i)
  elif 15 < trad1.loc[i]['도수'] <= 25:
    user_level4_sool.append(i)
  elif 25 < trad1.loc[i]['도수'] <= 40:
    user_level5_sool.append(i)
  else:
    user_level6_sool.append(i)

#나라 별 구분
##분류 기준
wine = ['과실주', '청주', '약주, 청주', '살균약주', '약주']
beer = ['탁주', '살균탁주']
spirits = ['리큐르', '증류식소주', '일반증류주', '증류주', '리큐르/기타주류']

##각 전통주가 wine, beer, spirits 어디에 들어가는지
# 술담화
wine_trad = []
beer_trad = []
spirits_trad = []

for i in range(len(trad)):
    if trad.iloc[i][5] in wine:
        wine_trad.append(trad.iloc[i][0])
    elif trad.iloc[i][5] in beer:
        beer_trad.append(trad.iloc[i][0])
    elif trad.iloc[i][5] in spirits:
        spirits_trad.append(trad.iloc[i][0])

# the sool
wine_trad1 = []
beer_trad1 = []
spirits_trad1 = []

for i in range(len(trad1)):
    if trad1.iloc[i][4] in wine:
        wine_trad1.append(trad1.iloc[i][0])
    elif trad1.iloc[i][4] in beer:
        beer_trad1.append(trad1.iloc[i][0])
    elif trad1.iloc[i][4] in spirits:
        spirits_trad1.append(trad1.iloc[i][0])

def cos_sim(A, B):
  if norm(A)*norm(B) == 0:
    if norm(A) == 0 and norm(B) == 0:
      return 1
    else:
      return 0
  else:
    return dot(A, B)/(norm(A)*norm(B))

#함수화 (입력 list, view)
def liquor_recommendation(INPUT, view):
    ##리스트에서 데이터 받기
    user_data = INPUT[0]
    user_liquor = liquor[liquor['Name'].isin(user_data)]
    user_data_abv = INPUT[2]
    user_data_country = INPUT[1][0]
    user_country_list = []
    
    for i in range(len(countries)):
        if countries['Country'][i] == user_data_country:
            user_country_list.append(countries['Wine'][i])
            user_country_list.append(countries['Beer'][i])
            user_country_list.append(countries['Spirits'][i])

    ##제조법 별 구분 - 구분진행
    make = []
    for i in user_data:
        if user_liquor['Type'][user_liquor.index[(user_liquor['Name'] == i)].to_list()[0]] == "Fermented":
            make.append(1)
        else:
            make.append(0)

    # make의 1과 0 비율
    count_fermented = 0
    count_distilled = 0

    for i in make:
        if i == 1:
            count_fermented += 1
        else:
            count_distilled += 1

    make_ratio = [count_fermented, count_distilled]

    # 재료 별 구분 - 구분 진행
    # 재료 벡터 [gin, grain, grain_etc, spices, fruit, whiskey, citrus, grape, floral]
    ingredients = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    distinguish = [gin, grain, grain_etc, spices, fruit, whiskey, citrus, grape, floral]

    for i in user_data:
        i = user_liquor.index[(user_liquor['Name'] == i)].to_list()[0]
        for j in range(len(distinguish)):
            for k in range(len(user_liquor['Main Ingredients'][i])):
                if user_liquor['Main Ingredients'][i][k] in distinguish[j]:
                    ingredients[j] += 1

    ingredients_liquor = []
    ingredients_liquor1 = []

    for i in range(len(ingredients)):
        if ingredients[i] > 0:
            if i == 0:
                ingredients_liquor.append(gin_trad)
                ingredients_liquor1.append(gin_trad1)
            elif i == 1:
                ingredients_liquor.append(grain_trad)
                ingredients_liquor1.append(grain_trad1)
            elif i == 2:
                ingredients_liquor.append(grain_etc_trad)
                ingredients_liquor1.append(grain_etc_trad1)
            elif i == 3:
                ingredients_liquor.append(spices_trad)
                ingredients_liquor1.append(spices_trad1)
            elif i == 4:
                ingredients_liquor.append(fruit_trad)
                ingredients_liquor1.append(fruit_trad1)
            elif i == 5:
                ingredients_liquor.append(whiskey_trad)
                ingredients_liquor1.append(whiskey_trad1)
            elif i == 6:
                ingredients_liquor.append(citrus_trad)
                ingredients_liquor1.append(citrus_trad1)
            elif i == 7:
                ingredients_liquor.append(grape_trad)
                ingredients_liquor1.append(grape_trad1)
            elif i == 8:
                ingredients_liquor.append(floral_trad)
                ingredients_liquor1.append(floral_trad1)

    ingredients_liquor = list(sum(ingredients_liquor, []))
    ingredients_liquor.sort(key=lambda x: x)

    ingredients_liquor1 = list(sum(ingredients_liquor1, []))
    ingredients_liquor1.sort(key=lambda x: x)

    # [num, 겹치는 개수]
    ingredients_liquor_number = []
    ingredients_liquor_number1 = []

    # 술담화
    i = 0
    while i in range(len(ingredients_liquor)):
        ingredients_liquor_number.append([ingredients_liquor[i], ingredients_liquor.count(ingredients_liquor[i])])
        if ingredients_liquor.count(ingredients_liquor[i]) > 0:
            i += ingredients_liquor.count(ingredients_liquor[i])
        else:
            i += 1

    # the sool
    i = 0
    while i in range(len(ingredients_liquor1)):
        ingredients_liquor_number1.append([ingredients_liquor1[i], ingredients_liquor1.count(ingredients_liquor1[i])])
        if ingredients_liquor1.count(ingredients_liquor1[i]) > 0:
            i += ingredients_liquor1.count(ingredients_liquor1[i])
        else:
            i += 1

    # 맛 별 비교 - 코사인유사도
    taste_user_liquor = user_liquor[['Bitter', 'Sweet', 'Sour', 'Spicy', 'Salty', 'Carbonated']]
    taste_user_liquor_list = np.array(taste_user_liquor.values.tolist())

    # 술담화
    similarity_taste = []

    for i in range(len(taste_user_liquor_list)):
        for j in range(len(taste_trad_list)):
            similarity_taste.append([i, j, cos_sim(taste_user_liquor_list[i], taste_trad_list[j])])

    # the sool
    similarity_taste1 = []

    for i in range(len(taste_user_liquor_list)):
        for j in range(len(taste_trad1_list)):
            similarity_taste1.append([i, j, cos_sim(taste_user_liquor_list[i], taste_trad1_list[j])])
    
    # 사용자 선택과 cos유사도 결과 평균
    similarity_taste_add = []
    similarity_taste_add1 = []

    # 술담화
    for i in range(len(taste_trad_list)):
        add = 0
        for j in range(len(similarity_taste)):
            if similarity_taste[j][1] == i:
                add += similarity_taste[j][2]
        # 평균
        similarity_taste_add.append([i, add / len(taste_user_liquor_list)])

    # the sool
    for i in range(len(taste_trad1_list)):
        add = 0
        for j in range(len(similarity_taste1)):
            if similarity_taste1[j][1] == i:
                add += similarity_taste1[j][2]
        # 평균
        similarity_taste_add1.append([i, add / len(taste_user_liquor_list)])

    similarity_taste_add.sort(key=lambda x: -x[1])
    similarity_taste_add1.sort(key=lambda x: -x[1])

    #도수 별 구분 - 구분 진행
    ##사용자 선택 도수 데이터만 추출
    # 술담화
    trad_abv = []

    for i in range(len(user_data_abv)):
        if user_data_abv[i] == 'level1':
            trad_abv += user_level1_damwha
        elif user_data_abv[i] == 'level2':
            trad_abv += user_level2_damwha
        elif user_data_abv[i] == 'level3':
            trad_abv += user_level3_damwha
        elif user_data_abv[i] == 'level4':
            trad_abv += user_level4_damwha
        elif user_data_abv[i] == 'level5':
            trad_abv += user_level5_damwha
        else:
            trad_abv += user_level6_damwha

    # the_sool
    trad1_abv = []

    for i in range(len(user_data_abv)):
        if user_data_abv[i] == 'level1':
            trad1_abv += user_level1_sool
        elif user_data_abv[i] == 'level2':
            trad1_abv += user_level2_sool
        elif user_data_abv[i] == 'level3':
            trad1_abv += user_level3_sool
        elif user_data_abv[i] == 'level4':
            trad1_abv += user_level4_sool
        elif user_data_abv[i] == 'level5':
            trad1_abv += user_level5_sool
        else:
            trad1_abv += user_level6_sool

    #추천
    ##지정된 도수에 있는 데이터에 있는 재료 벡터 뽑기
    abv_ingredients_liquor_number_list = []
    abv_ingredients_liquor_number1_list = []

    # 술담화
    for i in range(len(ingredients_liquor_number)):
        if ingredients_liquor_number[i][0] in trad_abv:
            abv_ingredients_liquor_number_list.append(ingredients_liquor_number[i])

    # the sool
    for i in range(len(ingredients_liquor_number1)):
        if ingredients_liquor_number1[i][0] in trad1_abv:
            abv_ingredients_liquor_number1_list.append(ingredients_liquor_number1[i])

    ##재료 기준 데이터에 맛 기준 데이터 엮기
    # 술담화
    ingredients_similarity_taste_add = []
    similarity_taste_add_ex = similarity_taste_add

    for i in range(len(abv_ingredients_liquor_number_list)):
        for j in range(len(similarity_taste_add)):
            if abv_ingredients_liquor_number_list[i][0] == similarity_taste_add[j][0]:
                similarity_taste_add_ex[j].append(abv_ingredients_liquor_number_list[i][1])
                ingredients_similarity_taste_add.append(similarity_taste_add_ex[j])

    # the sool
    ingredients_similarity_taste_add1 = []
    similarity_taste_add_ex1 = similarity_taste_add1

    for i in range(len(abv_ingredients_liquor_number1_list)):
        for j in range(len(similarity_taste_add1)):
            if abv_ingredients_liquor_number1_list[i][0] == similarity_taste_add1[j][0]:
                similarity_taste_add_ex1[j].append(abv_ingredients_liquor_number1_list[i][1])
                ingredients_similarity_taste_add1.append(similarity_taste_add_ex1[j])

    # 재료 벡터 count 내림차순 -> 유사도 내림차순
    ingredients_similarity_taste_add.sort(key=lambda x: (-x[2], -x[1]))
    ingredients_similarity_taste_add1.sort(key=lambda x: (-x[2], -x[1]))

    ##나라 구분 데이터 넣기 (유사도가 같을 경우 구분)
    # 술담화
    # user_country_list = [wine, beer, spirits]

    for i in range(len(ingredients_similarity_taste_add)):
        if ingredients_similarity_taste_add[i][0] in wine_trad:
            ingredients_similarity_taste_add[i].append(user_country_list[0])
        elif ingredients_similarity_taste_add[i][0] in beer_trad:
            ingredients_similarity_taste_add[i].append(user_country_list[1])
        elif ingredients_similarity_taste_add[i][0] in spirits_trad:
            ingredients_similarity_taste_add[i].append(user_country_list[2])
        else:
            ingredients_similarity_taste_add[i].append(0)

    # the sool
    for i in range(len(ingredients_similarity_taste_add1)):
        if ingredients_similarity_taste_add1[i][0] in wine_trad:
            ingredients_similarity_taste_add1[i].append(user_country_list[0])
        elif ingredients_similarity_taste_add1[i][0] in beer_trad:
            ingredients_similarity_taste_add1[i].append(user_country_list[1])
        elif ingredients_similarity_taste_add1[i][0] in spirits_trad:
            ingredients_similarity_taste_add1[i].append(user_country_list[2])
        else:
            ingredients_similarity_taste_add1[i].append(0)

    ##양조 vs 증류 구분하기
    # Fermented or Distilled?

    # 술담화
    ingredients_similarity_taste_add_fermented = []
    ingredients_similarity_taste_add_distilled = []

    for i in range(len(ingredients_similarity_taste_add)):
        if ingredients_similarity_taste_add[i][0] in fermented_trad:
            ingredients_similarity_taste_add_fermented.append(ingredients_similarity_taste_add[i])
        elif ingredients_similarity_taste_add[i][0] in distilled_trad:
            ingredients_similarity_taste_add_distilled.append(ingredients_similarity_taste_add[i])

    # the sool
    ingredients_similarity_taste_add1_fermented = []
    ingredients_similarity_taste_add1_distilled = []

    for i in range(len(ingredients_similarity_taste_add1)):
        if ingredients_similarity_taste_add1[i][0] in fermented_trad1:
            ingredients_similarity_taste_add1_fermented.append(ingredients_similarity_taste_add1[i])
        elif ingredients_similarity_taste_add1[i][0] in distilled_trad1:
            ingredients_similarity_taste_add1_distilled.append(ingredients_similarity_taste_add1[i])
    ##술담화 the sool 합치기
    # 이름 붙이기

    # 술담화
    for i in range(len(ingredients_similarity_taste_add_fermented)):
        ingredients_similarity_taste_add_fermented[i].append('술담화')

    for i in range(len(ingredients_similarity_taste_add_distilled)):
        ingredients_similarity_taste_add_distilled[i].append('술담화')

    # the sool
    for i in range(len(ingredients_similarity_taste_add1_fermented)):
        ingredients_similarity_taste_add1_fermented[i].append('the sool')

    for i in range(len(ingredients_similarity_taste_add1_distilled)):
        ingredients_similarity_taste_add1_distilled[i].append('the sool')

    # 리스트 합치기

    # 양조
    ingredients_similarity_taste_fermented_all = ingredients_similarity_taste_add_fermented + ingredients_similarity_taste_add1_fermented
    ingredients_similarity_taste_fermented_all.sort(key=lambda x: (-x[2], -x[1], -x[3]))

    # 증류
    ingredients_similarity_taste_distilled_all = ingredients_similarity_taste_add_distilled + ingredients_similarity_taste_add1_distilled
    ingredients_similarity_taste_distilled_all.sort(key=lambda x: (-x[2], -x[1], -x[3]))

    ##제조법 비율에 맞게 추출
    # 제조법 비율
    add = sum(make_ratio)
    for i in range(len(make_ratio)):
        make_ratio[i] = make_ratio[i] / add
    for i in range(len(make_ratio)):
        make_ratio[i] = make_ratio[i] * view
        make_ratio[i] = int(make_ratio[i])

    if sum(make_ratio) < view:
        make_ratio[make_ratio.index(min(make_ratio))] += 1

    ##리스트가 추출하는 값보다 작을 경우 예외처리
    # 둘 다 부족한 경우
    if len(ingredients_similarity_taste_distilled_all) < make_ratio[1] and len(
            ingredients_similarity_taste_fermented_all) < make_ratio[0]:
        make_ratio[0] = len(ingredients_similarity_taste_fermented_all)
        make_ratio[1] = len(ingredients_similarity_taste_distilled_all)
        print("일치하는 전통주 데이터가 부족합니다.")

    # fermented가 부족한 경우
    elif len(ingredients_similarity_taste_fermented_all) < make_ratio[0]:
        make_ratio[0] = len(ingredients_similarity_taste_fermented_all)
        make_ratio[1] += view - len(ingredients_similarity_taste_fermented_all)

    # distilled가 부족한 경우
    elif len(ingredients_similarity_taste_distilled_all) < make_ratio[1]:
        make_ratio[0] += view - len(ingredients_similarity_taste_distilled_all)
        make_ratio[1] = len(ingredients_similarity_taste_distilled_all)

    final_list_fermented = []
    final_list_distilled = []

    i = 0
    while i < make_ratio[0]:
        final_list_fermented.append(ingredients_similarity_taste_fermented_all[i])
        i += 1

    i = 0
    while i < make_ratio[1]:
        final_list_distilled.append(ingredients_similarity_taste_distilled_all[i])
        i += 1

    final_fermented = []
    for i in range(len(final_list_fermented)):
        final_fermented.append([final_list_fermented[i][0], final_list_fermented[i][4]])

    final_distilled = []
    for i in range(len(final_list_distilled)):
        final_distilled.append([final_list_distilled[i][0], final_list_distilled[i][4]])

    #리스트 합치기
    final_list = final_fermented + final_distilled

    return final_list

#함수 실행
INPUT = [['Gin', 'Gin and Tonic', 'Long Island Iced Tea', 'Lager Beer'], ['US'], ['level3', 'level2', 'level6']]

print(liquor_recommendation(INPUT,10))

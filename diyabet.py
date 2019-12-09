# -*- coding: utf-8 -*-

def diyabet_skorlama():
  while True:
    print('1) Cinsiyet: ')
    print('A: Erkek B: Kadın')
    gender = str(input())
    if gender.upper() == 'A' or gender.upper() == 'ERKEK':
      gender = gender
      break
    elif gender.upper() == 'B' or gender.upper() == 'KADIN':
      gender = gender
      break
    else:
      print('Uyarı: Yanlış ya da eksik cinsiyet bilgisi girdiniz. Lütfen yeniden deneyiniz.')
  while True: 
    age = input('2) Yaş: ')
    try:
      age = int(age)
      if age < 45:
        score_1 = 0
        break
      elif 45 <= age <= 54:
        score_1 = 2
        break
      elif 55 <= age <= 64:
        score_1 = 3
        break
      elif 64 < age:
        score_1 = 4
        break
    except:
      print('Uyarı: Yanlış yaş bilgisi girdiniz. Lütfen yeniden deneyiniz.')
  while True:
    b_m_i = input('3) Beden Kütle İndeksi(Kg/m2): ')
    try:
      b_m_i = int(b_m_i)
      if b_m_i < 25:
        score_2 = 0
        break
      elif 25 <= b_m_i <= 30:
        score_2 = 1
        break
      elif 30 < b_m_i:
        score_2 = 3
        break
    except:
      print('Uyarı: Yanlış beden kütle indeksi girdiniz. Lütfen yeniden deneyiniz.')
  while True:
    waist_circumference = input('4) Bel Çevresi(cm): ')
    try:
      if gender.upper() == 'A' or gender.upper() == 'ERKEK':
        waist_circumference = int(waist_circumference)
        if waist_circumference < 94:
          score_3 = 0
          break
        elif 94 <= waist_circumference <= 102:
          score_3 = 3
          break
        elif 102 < waist_circumference:
          score_3 = 4
          break
      elif gender.upper() == 'B' or gender.upper() == 'KADIN':
        waist_circumference = int(waist_circumference)
        if waist_circumference < 80:
          score_3 = 0
          break
        elif 80 <= waist_circumference <= 88:
          score_3 = 3
          break
        elif 88 < waist_circumference:
          score_3 = 4
          break
    except:
      print('Uyarı: Yanlış bel çevresi bilgisi girdiniz. Lütfen yeniden deneyiniz.')
  while True:
    print('5) Ekseri günlerde işte veya boş zamanlarınızda çoğunlukla günde en az 30 dakika egzersiz yapıyor musunuz?')
    print('A: Evet B: Hayır')
    exercise = str(input())
    try:
      if exercise.upper() == 'A' or exercise.upper() == 'EVET':
        score_4 = 0
        break
      elif exercise.upper() == 'B' or exercise.upper() == 'HAYIR':
        score_4 = 2
        break
      else:
        print('Uyarı: Yanlış bilgi girdiniz. Lütfen yeniden deneyiniz.')
    except:
      print('')
  while True:
    print('6) Hangi sıklıkla sebze-meyve tüketiyorsunuz?')
    print('A: Her gün B: Her gün değil')
    fruits_vegetables = str(input())
    try:
      if fruits_vegetables.upper() == 'A' or fruits_vegetables.upper() == 'HER GÜN':
        score_5 = 0
        break
      elif fruits_vegetables.upper() == 'B' or fruits_vegetables.upper() == 'HER GÜN DEĞİL':
        score_5 = 2
        break
      else:
        print('Uyarı: Yanlış bilgi girdiniz. Lütfen yeniden deneyiniz.')
    except:
      print('')
  while True:
    print('7) Kan basıncı yüksekliği için hiç ilaç kullandınız mı veya sizde yüksek tansiyon bulundu mu?')
    print('A: Hayır B: Evet')
    blood_pressure = str(input())
    try:
      if blood_pressure.upper() == 'A' or blood_pressure.upper() == 'HAYIR':
        score_6 = 0
        break
      elif blood_pressure.upper() == 'B' or blood_pressure.upper() == 'EVET':
        score_6 = 2
        break
      else:
        print('Uyarı: Yanlış bilgi girdiniz. Lütfen yeniden deneyiniz.')
    except:
      print('')
  while True:
    print('8) Hekim veya herahngi bir sağlık personeli tarafından (check-up, hastalık veya gebelik sırasında) kan şekerinizin yüksek veya sınırında olduğu söylendi mi?')
    print('A: Hayır B: Evet')
    sugar_in_blood = str(input())
    try:
      if sugar_in_blood.upper() == 'A' or sugar_in_blood.upper() == 'HAYIR':
        score_7 = 0
        break
      elif sugar_in_blood.upper() == 'B' or sugar_in_blood.upper() == 'EVET':
        score_7 = 5
        break
      else:
        print('Uyarı: Yanlış bilgi girdiniz. Lütfen yeniden deneyiniz.')
    except:
      print('')
  while True:
    print('9) Aile bireylerinizden herhangi birinde diyabet tanısı konulmuş muydu?')
    print('A: Hayır B: Evet, amca, hala dayı, teyze, kuzen ya da yeğen (2. derece yakınlarda) C: Evet, biyolojik baba ya da anne, kardeşler, ya da çocuğunuzda (1. derece yakınlarda)')
    diabetes_diagnosis = str(input())
    try:
      if diabetes_diagnosis.upper() == 'A' or diabetes_diagnosis.upper() == 'HAYIR':
        score_8 = 0
        break
      elif diabetes_diagnosis.upper() == 'B' or diabetes_diagnosis.upper() == 'EVET, AMCA, HALA, DAYI, TEYZE, KUZEN, YA DA YEĞEN (2. DERECE YAKINLARDA)':
        score_8 = 3
        break
      elif diabetes_diagnosis.upper() == 'C' or diabetes_diagnosis.upper() == 'EVET, BIYOLOJIK BABA YA DA ANNE, KARDEŞLER, YA DA ÇOCUĞUNUZDA (1. DERECE YAKINLARDA)':
        score_8 = 5
        break
      else:
        print('Uyarı: Yanlış bilgi girdiniz. Lütfen yeniden deneyiniz.')
    except:
      print('')
  try:
    score_total = score_1 + score_2 + score_3 + score_4 + score_5 + score_6 + score_7 + score_8
    if score_total < 7:
      print('Risk derecesi: Düşük')
      print('10 yıllık risk: %1 (1/100)')
    elif 7 <= score_total <= 11:
      print('Risk derecesi: Hafif')
      print('10 yıllık risk: % (1/25)')
    elif 12 <= score_total <= 14:
      print('Risk derecesi: Orta')
      print('10 yıllık risk: %16 (1/6)')
    elif 15 <= score_total <= 20:
      print('Risk derecesi: Yüksek')
      print('10 yıllık risk: %33 (1/3)')
    elif 20 < score_total:
      print('Risk derecesi: Çok yüksek')
      print('10 yıllık risk: %50 (1/2)')
  except:
    print('Uyarı: Bir veya birden çok soruya yanlış bilgi girildiği için skorlama yapılamamaktadır.')
diyabet_skorlama()

# 2023-2024 Global Air Quality: PM2.5

![image](https://imgur.com/9Smq6ou.jpg)


## Project Description
This project aims to analyze global air quality using PM2.5 data from [World Air Quality Data 2024 (Updated)](https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated), which includes data from 8,469 stations in 65 countries, with PM2.5 being the main parameter used for analysis. The project showcases an overall picture of PM2.5 pollution levels from the years 2023-2024 on a geographic map with Scatter Plots on Mapbox, which helps in exploring differences in PM2.5 pollution levels in different areas.


## Data and Data Source
[World Air Quality Data 2024 (Updated)](https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated) มีการรวบรวมการตรวจวัดคุณภาพอากาศจากสถานที่ 8,469 แห่งใน 65 ประเทศ ข้อมูลถูกรวบรวมจากแหล่งข้อมูลระดับรัฐบาลและระดับการวิจัย 105 แห่งโดย [OpenAQ](https://public.opendatasoft.com/explore/dataset/openaq/export/?disjunctive.city&disjunctive.location&disjunctive.measurements_parameter&sort=measurements_lastupdated&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibWVhc3VyZW1lbnRzX3ZhbHVlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoicmFuZ2UtY3VzdG9tIn1dLCJ4QXhpcyI6Im1lYXN1cmVtZW50c19sYXN0dXBkYXRlZCIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJtZWFzdXJlbWVudHNfcGFyYW1ldGVyIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJvcGVuYXEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmNpdHkiOnRydWUsImRpc2p1bmN0aXZlLmxvY2F0aW9uIjp0cnVlLCJkaXNqdW5jdGl2ZS5tZWFzdXJlbWVudHNfcGFyYW1ldGVyIjp0cnVlLCJzb3J0IjoibWVhc3VyZW1lbnRzX2xhc3R1cGRhdGVkIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=2,2.98693,49.21875&basemap=jawg.light) 
ข้อมูลแต่ละรายการมีรายละเอียดพารามิเตอร์คุณภาพอากาศที่สำคัญ อาทิ PM2.5, NO2, SO2, CO และ O3 ตั้งแต่ปี 2015 จนถึงเดือนมีนาคม 2024 พร้อมทั้งพิกัดทางภูมิศาสตร์ ชุดข้อมูลนี้จึงเป็นแหล่งข้อมูลที่เหมาะสมในการทำความเข้าใจสถานะปัจจุบันและแนวโน้มของคุณภาพอากาศทั่วโลก 

PM2.5 เป็นฝุ่นละอองในบรรยากาศที่มีขนาดเล็ก บางเบา และมีผลกระทบด้านลบต่อสุขภาพของประชากร จากการที่อนุภาค PM2.5 มีขนาดเล็กจึงสามารถลอยตัวอยู่ในอากาศได้นานกว่าอนุภาคอื่น เป็นการเพิ่มโอกาสให้ PM2.5 สามารถเข้าสู่ร่างกายของมนุษย์ได้มากขึ้นผ่านการหายใจ ซึ่งสามารถกระตุ้นหรือส่งผลต่อโรคบางชนิดให้มีอาการแย่ลง เช่น โรคหอบหืด โรคหัวใจ โรคหลอดลมอักเสบ หรือโรคทางเดินหายใจอื่น ๆ ตามที่งานวิจัยในวารสาร American Medical Association ได้ระบุไว้ว่า การเผชิญกับ PM2.5 ต่อเนื่องกันเป็นระยะเวลานานจะนำไปสู่การเกิดผลึกตะกอนในหลอดเลือดแดง ซึ่งเป็นสาเหตุของการอักเสบของหลอดเลือด ทำให้หลอดเลือดแดงแข็งตัวขึ้นซึ่งอาจเป็นสาเหตุของการเกิดโรคหัวใจและโรคหลอดเลือดในสมองตามมาได้ งานในครั้งนี้จึงสนใจศึกษา PM2.5 เป็นหลัก
     

## Distribution of PM2.5 Pollution Levels - Visualize with Scatter Plots on Mapbox
Scatter Plots บน Mapbox แสดงภาพระดับมลพิษ PM2.5 ในพื้นที่ต่าง ๆ ด้วยความสามารถในการแสดงข้อมูลที่เกี่ยวข้องกับพิกัดทางภูมิศาสตร์ โดยสีของจุดแสดงถึงระดับมลพิษ PM2.5 ที่ตรงกับตำแหน่งที่ตรวจวัดคุณภาพอากาศ แสดงให้เห็นภาพรวมของระดับมลพิษ PM2.5 โดยเฉลี่ยต่อปีในพื้นที่ต่าง ๆ ช่วยให้ผู้ชมเข้าใจและรับรู้ถึงสถานการณ์ของระดับมลพิษ PM2.5 ในอากาศของปีที่ผ่านมาได้โดยง่าย ด้วยการแบ่งระดับความรุนแรงของมลพิษ PM2.5 ตามสี และมาตรฐานคุณภาพอากาศจาก The National Ambient Air Quality Standards for Particle Pollution :

* สีเขียว : ระดับ "Low"
* สีเหลือง : ระดับ "Moderate"
* สีส้ม : ระดับ "Unhealthy for Sensitive Groups"
* สีแดง : ระดับ "Unhealthy"
* สีม่วง : ระดับ "Very Unhealthy"

นอกจากนี้ แผนที่ระดับมลพิษ PM2.5 สามารถนำไปประกอบการตัดสินใจในการศึกษาหรือกิจกรรมอื่น ๆ ได้อย่างมีประสิทธิภาพ ซึ่งอาจสำรวจเพิ่มเติมในพื้นที่ที่มี PM 2.5 ในระดับ “Very Unhealthy” เพื่อระบุถึงสาเหตุของมลพิษดังกล่าวและหาแนวทางแก้ไข หรือการดำเนินการที่จำเป็นในการควบคุมมลพิษต่อไป เช่น พื้นที่บริเวณดังกล่าวตั้งอยู่ใกล้กับสนามบินหรือโรงงานอุตสาหกรรม อาจดำเนินการหามาตรการที่เหมาะสมในการควบคุมระดับมลพิษ เพื่อใม่ให้ส่งผลกระทบต่อสุขภาพของประชากรในบริเวณดังกล่าว


## Observation
จากแผนที่ระดับมลพิษ PM2.5 พบว่า ระดับ PM2.5 ที่อยู่ในระดับ "Unhealthy" กระจายอยู่ในทวีปยุโรปและในเมืองต่าง ๆ ของเม็กซิโกที่ตั้งอยู่ตอนล่างของทวีปอเมริกาเหนือ ตลอดจนมีการกระจุกตัวอยู่พื้นที่ตอนบนหรือภาคเหนือของไทย ที่ซึ่งมี PM2.5 ในระดับ "Very Unhealthy" บริเวณพื้นที่ที่ติดกับประเทศเมียนมาร์อยู่ด้วยเช่นเดียวกัน

ทั้งนี้ พื้นที่ที่มีข้อมูลระดับมลพิษ PM2.5 ในปี 2023-2024 ส่วนใหญ่อยู่ในทวีปอเมริกาเหนือกับยุโรป ซึ่งมีระดับ PM2.5 "Low" และ "Moderate" เป็นส่วนมาก

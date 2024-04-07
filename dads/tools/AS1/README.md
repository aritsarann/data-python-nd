## 2023-2024 World Air Quality : PM2.5

![image](https://imgur.com/9Smq6ou.jpg)

### About Dataset
ข้อมูลที่ใช้ในการสร้าง chart นี้จาก [World Air Quality Data 2024 (Updated)](https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated) ที่มีการรวบรวมการตรวจวัดคุณภาพอากาศจากสถานที่ 8,469 แห่งใน 65 ประเทศ ข้อมูลถูกรวบรวมจากแหล่งข้อมูลระดับรัฐบาลและระดับการวิจัย 105 แห่งโดย [OpenAQ](https://public.opendatasoft.com/explore/dataset/openaq/export/?disjunctive.city&disjunctive.location&disjunctive.measurements_parameter&sort=measurements_lastupdated&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibWVhc3VyZW1lbnRzX3ZhbHVlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoicmFuZ2UtY3VzdG9tIn1dLCJ4QXhpcyI6Im1lYXN1cmVtZW50c19sYXN0dXBkYXRlZCIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJtZWFzdXJlbWVudHNfcGFyYW1ldGVyIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJvcGVuYXEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmNpdHkiOnRydWUsImRpc2p1bmN0aXZlLmxvY2F0aW9uIjp0cnVlLCJkaXNqdW5jdGl2ZS5tZWFzdXJlbWVudHNfcGFyYW1ldGVyIjp0cnVlLCJzb3J0IjoibWVhc3VyZW1lbnRzX2xhc3R1cGRhdGVkIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=2,2.98693,49.21875&basemap=jawg.light) 

ข้อมูลแต่ละรายการมีรายละเอียดพารามิเตอร์คุณภาพอากาศที่สำคัญตั้งแต่ปี 2015 จนถึงเดือนมีนาคม 2024 พร้อมทั้งสารมลพิษ (Pollutants) ที่หลากหลาย เช่น PM2.5, NO2, SO2, CO และ O3 ชุดข้อมูลนี้จึงเป็นแหล่งข้อมูลสำคัญในการทำความเข้าใจสถานะปัจจุบันและแนวโน้มของคุณภาพอากาศทั่วโลก ซึ่งได้เลือกใช้ข้อมูลสารมลพิษ PM2.5 ในหน่วยไมโครกรัมต่อลูกบาศก์เมตร (μg/m3) ประจำปี 2023-2024 ในการวิเคราะห์ครั้งนี้เป็นหลัก

### Scatter Plots on Mapbox
การเลือกแสดงแผนที่แสดงระดับมลพิษ PM 2.5 ด้วย Scatter Plots on Mapbox เนื่องจากแผนภาพชนิดนี้สามารถแสดงข้อมูลที่เกี่ยวข้องกับพิกัดทางภูมิศาสตร์ได้อย่างชัดเจน โดยสีของจุดแสดงระดับมลพิษที่ตรงกับตำแหน่งที่ตรวจวัดคุณภาพอากาศแสดงให้เห็นภาพรวมของค่าเฉลี่ยระดับมลพิษ PM 2.5 ในพื้นที่ประเทศต่าง ๆ รวมถึงแสดงให้ผู้ชมเข้าใจ รับรู้ถึงสถานการณ์ของระดับมลพิษ PM 2.5 ในอากาศของปีที่ผ่านมาได้โดยง่าย ด้วยการแบ่งระดับความรุนแรงของมลพิษ PM 2.5 ตามสีและระดับความรุนแรงจาก The National Ambient Air Quality Standards for Particle Pollution คือ 
* สีเขียว ในระดับ "Low"
* สีเหลือง ในระดับ "Moderate"
* สีส้ม ในระดับ "Unhealthy for Sensitive Groups"
* สีแดง ในระดับ "Unhealthy"
* สีม่วง ในระดับ "Very Unhealthy"

นอกจากนี้ แผนที่แสดงระดับมลพิษ PM 2.5 สามารถนำไปประกอบการตัดสินใจในการศึกษาหรือกิจกรรมอื่น ๆ ได้อย่างมีประสิทธิภาพ ซึ่งอาจเจาะลึกลงไปในพื้นที่ที่ PM 2.5 มีค่าในระดับ “Very Unhealthy” เพื่อหาสาเหตุของระดับมลพิษดังกล่าวและหนทางแก้ไขต่อไป

โดยจากแผนที่ แสดงให้เห็นว่า ระดับ PM 2.5 ในระดับ "Unhealthy" มีการกระจายอยู่ในทวีปยุโรป และกระจายตามเมืองต่าง ๆ ใน Mexica และมีการกระจุกตัวอยู่พื้นที่ตอนบนของประเทศไทย ที่ซึ่งมี PM 2.5 ในระดับ "Very Unhealthy" บริเวณที่ติดกับประเทศเมียนมาร์ด้วยเช่นเดียวกัน 

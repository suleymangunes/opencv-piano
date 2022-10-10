import cv2
import ultis
from multiprocessing.pool import ThreadPool

# hsv renk kodlari bulunmus oldu
low_hsv, up_hsv = ultis.hsvbul()

# perspektif yapilacak matrix degeri bulundu warppers ile persi alinir
matrix = ultis.pers_noktalari()

# notalari saklayacak roi noktalari bulundu
roilerim = ultis.roi_noktalari(matrix)
print("roilerim", roilerim)

cap = cv2.VideoCapture(1, cv2.CAP_DSHOW)

t1 = 0  # tuslarar sifir degeri baslangicta verilmeli ki belirlene fonkisyona uysun
t2 = 0
t3 = 0
t4 = 0
t5 = 0
t6 = 0
t7 = 0
t8 = 0
t9 = 0
t10 = 0
t11 = 0
t12 = 0
t13 = 0
t14 = 0
t15 = 0
t16 = 0
t17 = 0
t18 = 0
t19 = 0
t20 = 0
t21 = 0
t22 = 0
t23 = 0
t24 = 0
t25 = 0
t26 = 0
t27 = 0
t28 = 0
t29 = 0
t30 = 0
t31 = 0
t32 = 0
t33 = 0
t34 = 0
t35 = 0
t36 = 0
t37 = 0
t38 = 0
t39 = 0
t40 = 0
t41 = 0
t42 = 0
t43 = 0
t44 = 0
t45 = 0
t46 = 0
t47 = 0
t48 = 0
t49 = 0
t50 = 0
t51 = 0
t52 = 0
t53 = 0
t54 = 0
t55 = 0
t56 = 0
t57 = 0
t58 = 0
t59 = 0
t60 = 0
t61 = 0
t62 = 0
t63 = 0
t64 = 0
t65 = 0
t66 = 0
t67 = 0
t68 = 0
t69 = 0
t70 = 0
t71 = 0
t72 = 0
t73 = 0
t74 = 0
t75 = 0
t76 = 0
t77 = 0
t78 = 0
t79 = 0
t80 = 0
t81 = 0
t82 = 0
t83 = 0
t84 = 0
t85 = 0
t86 = 0
t87 = 0
t88 = 0

while True:
    ret, frame = cap.read()
    if ret == 0:
        break
    frame = cv2.resize(frame, (960, 540))
    frame = cv2.flip(frame, 1)
    # disardan alinen deger ile dst'ye pers uygulandi
    dst = cv2.warpPerspective(frame, matrix, (960, 540))
    # pers yapilmis deger uzerinde roileri gosteren dortgenler cizildi
    ultis.roi_dortgenleri(roilerim, dst)

    # thread ile tum sonfkiyonalarin eszamanli calimasi saglandi
    t1 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[0], t1, low_hsv, up_hsv))
    t1 = t1.get()
    t2 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[1], t2, low_hsv, up_hsv))
    t2 = t2.get()
    t3 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[2], t3, low_hsv, up_hsv))
    t3 = t3.get()
    t4 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[3], t4, low_hsv, up_hsv))
    t4 = t4.get()
    t5 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[4], t5, low_hsv, up_hsv))
    t5 = t5.get()
    t6 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[5], t6, low_hsv, up_hsv))
    t6 = t6.get()
    t7 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[6], t7, low_hsv, up_hsv))
    t7 = t7.get()
    t8 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[7], t8, low_hsv, up_hsv))
    t8 = t8.get()
    t9 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[8], t9, low_hsv, up_hsv))
    t9 = t9.get()
    t10 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[9], t10, low_hsv, up_hsv))
    t10 = t10.get()
    t11 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[10], t11, low_hsv, up_hsv))
    t11 = t11.get()
    t12 = ThreadPool(processes=1).apply_async(ultis.bottombul, (dst, roilerim, roilerim[11], t12, low_hsv, up_hsv))
    t12 = t12.get()
    cv2.imshow("frame", frame)
    cv2.imshow("dst", dst)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

public class tran{
    public static void main(String[] args){
        gsjw(2546524.0, 412884.0);
        gsjw(2575622.0, 450819.0);
    }
    public static void gsjw(double X ,double Y){
        double x,y,L0 = 0,B,L;
        x = X;
        y = Y;
        double p=206264.80625;
        for (int i = 1; Y/i >=10; i = i * 10)
        {
            y = Y - (int)(Y / i) * i-500000;
            L0 =117;
        }        
        double bt = x / 6367558.4969*p;
        double BT = x / 6367558.4969;
        double c3=Math.cos(BT)*Math.cos(BT);
        double c4=Math.sin(BT)*Math.cos(BT);
        double Bf=(bt+(50221746+(293622+(2350+22*c3)*c3)*c3)*c4*Math.pow(10,-10)*p)/p;
        double c5=Math.pow(Math.cos(Bf),2);
        double c6=Math.sin(Bf)*Math.cos(Bf);
        double Nf=6399698.902-(21562.267-(108.973-0.612*c5)*c5)*c5;
        double Z=y/(Nf*Math.cos(Bf));
        double b2 = (0.5 + 0.003369 * c5) * c6;
        double b3 = 0.333333 - (0.166667 - 0.001123 * c5) * c5;
        double b4 = 0.25 + (0.16161 + 0.00562 * c5) * c5;
        double b5=0.2-(0.1667-0.0088*c5)*c5;
        double z2=Math.pow(Z,2);
        B = (Bf*p - (1 - (b4 - 0.12 *z2) * z2) * z2 * b2 * p)/3600.0;
        L = L0+((1 - (b3 - b5 * z2) * z2) * Z * p)/3600.0;
        System.out.println("jingdu:"+L+"    weidu:"+B+"    zhongyangziwuxian:"+L0);
    }
}

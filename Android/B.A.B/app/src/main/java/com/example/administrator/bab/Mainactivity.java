package com.example.administrator.bab;

import android.content.Context;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.net.Uri;
import android.os.AsyncTask;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.LinearLayout;
import android.widget.TextView;
import android.widget.Toast;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

import java.io.IOException;
import java.text.SimpleDateFormat;
import java.util.Date;


public class Mainactivity extends AppCompatActivity {

    //변수 선언부
    LinearLayout Logo, Yesterday, Tomorrow;
    ImageButton Kakao, Finish, Web, Calendar, Developer;
    ImageView Bab;
    TextView Day, Meal;

    public static final String WIFI_STATE = "WIFE";               //wifi 상태 멤버 변수 선언
    public static final String MOBILE_STATE = "MOBILE";          //데이터 네트워크 상태 멤버 변수 선언
    public static final String NONE_STATE = "NONE";               //인터넷 환경이 연결되지 않은 상태 멤버 변수 선언

    public static int logo_num = 0;

    int month_num, day_num = 1, meal_num = 0, cnt = 0;
    int REQUEST_ACT;

    Elements contents_bf, contents_lc, contents_dn;
    Document doc = null;

    long now = System.currentTimeMillis();                                            //현재 시간
    Date date = new Date(now);

    String[][] bab = {{"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},       //급식메뉴가 담길 변수
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"},
            {"\0", "\0", "\0"}, {"\0", "\0", "\0"}, {"\0", "\0", "\0"}};


    SimpleDateFormat sdf_full = new SimpleDateFormat("MM월 dd일 (E)");        //현재 시간 표현 방식 변수를 다양하게 생성
    SimpleDateFormat sdf_month = new SimpleDateFormat("M");
    SimpleDateFormat sdf_day = new SimpleDateFormat("d");

    String getDate = sdf_full.format(date);                                     //현재 날짜를 String형으로 변환
    String getMonth = sdf_month.format(date);                                   //현재 월수를 String형으로 변환
    String getDay = sdf_day.format(date);                                       //현재 일수를 String형으로 변환

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Bab = (ImageView) findViewById(R.id.bab);                            //xml의 ID와 상응하는 객체를 찾는 메소드
        Finish = (ImageButton) findViewById(R.id.finish);
        Meal = (TextView) findViewById(R.id.meal);
        Logo = (LinearLayout) findViewById(R.id.logo);
        Yesterday = (LinearLayout) findViewById(R.id.button1);
        Tomorrow = (LinearLayout) findViewById(R.id.button2);
        Day = (TextView) findViewById(R.id.day);
        Kakao = (ImageButton) findViewById(R.id.kaka);
        Web = (ImageButton) findViewById(R.id.web);
        Developer = (ImageButton) findViewById(R.id.developer);
        Calendar = (ImageButton) findViewById(R.id.calendar);

        if(getWhatKindOfNetwork(getApplication()).equals("NONE")){
            finish();
            Toast.makeText(getApplicationContext(), "네트워크 연결 안됨", Toast.LENGTH_SHORT).show();
        }

        Intent intent = new Intent(this, Loading.class);                // 로딩화면 실행
        startActivity(intent);

        day_num = Integer.parseInt(getDay);                             //현재 일수를 정수형으로 변환
        month_num = Integer.parseInt(getMonth);                         //현재 달수를 정수형으로 변환

        Day.setText(getDate);                                           //현재날짜 출력

        new AsyncTask() {//AsyncTask객체 생성
            @Override
            protected Object doInBackground(Object[] params) {

                try {
                    doc = Jsoup.connect("http://www.inmagobab.ml/month").get();                        //inmagobab.ml html소스 불러오기

                    contents_bf = doc.select("body > bf > p > men");                            //조식 select문
                    contents_lc = doc.select("body > lc > p > men");                            //중식 select문
                    contents_dn = doc.select("body > dn > p > men");                            //석식 select문
                } catch (IOException e) {
                    e.printStackTrace();
                }

                cnt = 0;

                for (Element element : contents_bf) {
                    bab[cnt][0] = "\n\n[ 조식 메뉴 ]\n\n" + element.text().replace("/", "\n");      //조식 설정
                    cnt++;
                }

                cnt = 0;

                for (Element element : contents_lc) {
                    bab[cnt][1] = "\n\n[ 중식 메뉴 ]\n\n" + element.text().replace("/", "\n");      //중식 설정
                    cnt++;
                }

                cnt = 0;

                for (Element element : contents_dn) {
                    bab[cnt][2] = "\n\n[ 석식 메뉴 ]\n\n" + element.text().replace("/", "\n");      //석식 설정
                    cnt++;
                }
                return null;
            }

            protected void onPostExecute(Object o) {
                super.onPostExecute(o);
                Meal.setText(bab[day_num - 1][meal_num]);                //파싱 후 Textview에 출력되는 데이터
            }
        }.execute();

        Logo.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                change_logo();
            }
        });

        // 가장 처음 급식일 경우 Toast를 띄우고, 그 외에는 이전 급식을 보여주는 버튼 설정
        Yesterday.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (day_num == 1 & meal_num == 0)
                    Toast.makeText(getApplicationContext(), "첫 날입니다.", Toast.LENGTH_SHORT).show();
                else yesterday();
            }
        });

        // 마지막 급식일 경우 Toast를 띄우고, 그 외에는 다음 급식을 보여주는 버튼 설정
        Tomorrow.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (day_num == 30 & meal_num == 2)
                    Toast.makeText(getApplicationContext(), "마지막 날입니다.", Toast.LENGTH_SHORT).show();
                else tomorrow();
            }
        });

        Kakao.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                kakao();
            }
        });

        Calendar.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                calendar();
            }
        });

        Finish.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();
            }
        });

        Web.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                openweb();
            }
        });

        Developer.setOnClickListener(new View.OnClickListener() {
            public void onClick(View view) {
                information();
            }
        });
    }


    public void change_logo() {                  //로고 이미지 변화 함수
        logo_num++;
        switch (logo_num % 9) {
            case 0:
                Bab.setImageResource(R.drawable.bablogo_white);
                break;
            case 1:
                Bab.setImageResource(R.drawable.red);
                break;
            case 2:
                Bab.setImageResource(R.drawable.orange);
                break;
            case 3:
                Bab.setImageResource(R.drawable.yellow);
                break;
            case 4:
                Bab.setImageResource(R.drawable.green);
                break;
            case 5:
                Bab.setImageResource(R.drawable.skyblue);
                break;
            case 6:
                Bab.setImageResource(R.drawable.navy);
                break;
            case 7:
                Bab.setImageResource(R.drawable.violet);
                break;
            case 8:
                Bab.setImageResource(R.drawable.bablogo_white_knife);
                break;
            default:
                break;
        }

    }

    public void kakao() {
        if (Kakao.getId() == R.id.kaka) {
            Intent myIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://pf.kakao.com/_klMyC"));
            startActivity(myIntent);
        }
    }                       // 카톡 플러스친구 링크

    public void tomorrow() {
        if (meal_num >= 2) {
            day_num++;
            meal_num = 0;
            Meal.setText(bab[day_num - 1][meal_num]);

            getDate = month_num + "월 " + day_num + "일 " + "(" + eday() + ")";
            Day.setText(getDate);
        } else {
            meal_num++;
            Meal.setText(bab[day_num - 1][meal_num]);
        }
    }                     // 다음 급식 보여주는 함수

    public void yesterday() {
        if (meal_num <= 0) {
            day_num--;
            meal_num = 2;
            Meal.setText(bab[day_num - 1][meal_num]);

            getDate = month_num + "월 " + day_num + "일 " + "(" + eday() + ")";
            Day.setText(getDate);
        } else {
            meal_num--;
            Meal.setText(bab[day_num - 1][meal_num]);
        }
    }                    // 이전 급식 보여주는 함수

    public void openweb() {
        Intent yourIntent = new Intent(Intent.ACTION_VIEW, Uri.parse("http://inmagobab.ml"));
        startActivity(yourIntent);
    }                      // 인마고 밥 웹 페이지 링크

    public void calendar() {
        Intent intent = new Intent(getApplicationContext(), Calendar.class);
        startActivityForResult(intent, REQUEST_ACT);
    }                     // 월 급식으로 넘어가는 함수

    public void information() {
        Intent intent = new Intent(getApplicationContext(), Developer.class);
        startActivityForResult(intent, REQUEST_ACT);
    }                  // 개발자 정보 탭으로 넘어가는 함수

    public String eday() {
        String temp = "";
        switch (day_num % 7) {
            case 5:
                temp = "월";
                break;
            case 6:
                temp = "화";
                break;
            case 0:
                temp = "수";
                break;
            case 1:
                temp = "목";
                break;
            case 2:
                temp = "금";
                break;
            case 3:
                temp = "토";
                break;
            case 4:
                temp = "일";
                break;
            default:
                break;
        }
        return temp;
    }                       // 날짜와 함께 요일 출력하는 함수

    public static String getWhatKindOfNetwork(Context context){
        ConnectivityManager cm = (ConnectivityManager) context.getSystemService(Context.CONNECTIVITY_SERVICE);
        NetworkInfo activeNetwork = cm.getActiveNetworkInfo();
        if (activeNetwork != null) {
            if (activeNetwork.getType() == ConnectivityManager.TYPE_WIFI) {
                return WIFI_STATE;
            } else if (activeNetwork.getType() == ConnectivityManager.TYPE_MOBILE) {
                return MOBILE_STATE;
            }
        }
        return NONE_STATE;
    }

    protected void onActivityResult(int requestCode, int resultCode, Intent intent) {       //달력에서 클릭한 날짜의 급식 출력하는 함수
        super.onActivityResult(requestCode, resultCode, intent);

        if (requestCode == REQUEST_ACT) {
            if (intent != null) {
                String d = intent.getStringExtra("day");        // Calendar 클래스의 day인자를 d에 넘겨줌

                day_num = Integer.parseInt(d);                  // d 를 정수형으로 변환하여 day_num에 넣음

                Meal.setText(bab[day_num - 1][0]);
                getDate = month_num + "월 " + day_num + "일 " + "(" + eday() + ")";
                Day.setText(getDate);
            }
        }
    }
}


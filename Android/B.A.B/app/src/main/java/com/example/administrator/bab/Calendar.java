package com.example.administrator.bab;

import android.app.Activity;
import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

public class Calendar extends AppCompatActivity {

    Button t1028, t1029, t1030, t1031, t1101, t1102, t1103, t1104, t1105, t1106, t1107, t1108, t1109, t1110, t1111, t1112, t1113, t1114;
    Button t1115,t1116, t1117, t1118, t1119, t1120, t1121, t1122, t1123, t1124, t1125, t1126, t1127, t1128, t1129, t1130, t1201;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_calendar);

        t1028 = (Button)findViewById(R.id.I028);
        t1029 = (Button)findViewById(R.id.I029);
        t1030 = (Button)findViewById(R.id.I030);
        t1031 = (Button)findViewById(R.id.I031);
        t1101 = (Button)findViewById(R.id.I101);
        t1102 = (Button)findViewById(R.id.I102);
        t1103 = (Button)findViewById(R.id.I103);
        t1104 = (Button)findViewById(R.id.I104);
        t1105 = (Button)findViewById(R.id.I105);
        t1106 = (Button)findViewById(R.id.I106);
        t1107 = (Button)findViewById(R.id.I107);
        t1108 = (Button)findViewById(R.id.I108);
        t1109 = (Button)findViewById(R.id.I109);
        t1110 = (Button)findViewById(R.id.I110);
        t1111 = (Button)findViewById(R.id.I111);
        t1112 = (Button)findViewById(R.id.I112);
        t1113 = (Button)findViewById(R.id.I113);
        t1114 = (Button)findViewById(R.id.I114);
        t1115 = (Button)findViewById(R.id.I115);
        t1116 = (Button)findViewById(R.id.I116);
        t1117 = (Button)findViewById(R.id.I117);
        t1118 = (Button)findViewById(R.id.I118);
        t1119 = (Button)findViewById(R.id.I119);
        t1120 = (Button)findViewById(R.id.I120);
        t1121 = (Button)findViewById(R.id.I121);
        t1122 = (Button)findViewById(R.id.I122);
        t1123 = (Button)findViewById(R.id.I123);
        t1124 = (Button)findViewById(R.id.I124);
        t1125 = (Button)findViewById(R.id.I125);
        t1126 = (Button)findViewById(R.id.I126);
        t1127 = (Button)findViewById(R.id.I127);
        t1128 = (Button)findViewById(R.id.I128);
        t1129 = (Button)findViewById(R.id.I129);
        t1130 = (Button)findViewById(R.id.I130);
        t1201 = (Button)findViewById(R.id.I201);

        t1028.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1029.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1030.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1031.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1101.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("1");
            }
        });
        t1102.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("2");
            }
        });
        t1103.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1104.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1105.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("5");
            }
        });
        t1106.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("6");
            }
        });
        t1107.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("7");
            }
        });
        t1108.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("8");
            }
        });
        t1109.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("9");
            }
        });
        t1110.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1111.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1112.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("12");
            }
        });
        t1113.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("13");
            }
        });
        t1114.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("14");
            }
        });
        t1115.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("15");
            }
        });
        t1116.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("16");
            }
        });
        t1117.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1118.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1119.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("19");
            }
        });
        t1120.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("20");
            }
        });
        t1121.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("21");
            }
        });
        t1122.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("22");
            }
        });
        t1123.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("23");
            }
        });
        t1124.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1125.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
        t1126.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("26");
            }
        });
        t1127.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("27");
            }
        });
        t1128.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("28");
            }
        });
        t1129.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("29");
            }
        });
        t1130.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                bab("30");
            }
        });
        t1201.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                nope();
            }
        });
    }
    public void nope(){                         // 급식이 없는 날 출력하는 함수
        Toast.makeText(getApplicationContext(),"- 주말에는 급식이 없습니다 -",Toast.LENGTH_SHORT).show();
    }

    public void bab(String putDay){             // 클릭한 날짜의 급식으로 넘어가는 함수
        Intent resultIntent = new Intent();
        resultIntent.putExtra("day", putDay);                       //intent의 day인자에 putday 넘겨줌
        setResult(Activity.RESULT_OK, resultIntent);

        finish();
    }
}

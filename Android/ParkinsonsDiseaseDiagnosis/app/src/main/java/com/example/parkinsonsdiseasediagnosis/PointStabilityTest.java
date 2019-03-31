package com.example.parkinsonsdiseasediagnosis;

import android.app.Activity;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.res.AssetManager;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.Path;
import android.graphics.PorterDuff;
import android.graphics.PorterDuffXfermode;
import android.graphics.drawable.BitmapDrawable;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.MotionEvent;
import android.view.SurfaceHolder;
import android.view.SurfaceView;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;

import com.android.volley.AuthFailureError;
import com.android.volley.NetworkResponse;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.VolleyLog;
import com.android.volley.toolbox.HttpHeaderParser;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;


public class PointStabilityTest extends Activity {

    DrawingView dv ;
    private Paint mPaint;
    private Boolean oldState = true;

    ArrayList<float []> list = new ArrayList<>();

    private RequestQueue mRequestQueue;
    private StringRequest stringRequest;

    ArrayList<float[]> staticList;
    ArrayList<float[]> dynamicList;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        dv = new DrawingView(this);
        staticList = (ArrayList<float[]>) getIntent().getExtras().getSerializable("static");
        dynamicList = (ArrayList<float[]>) getIntent().getExtras().getSerializable("dynamic");
        setContentView(dv);
        mPaint = new Paint();
        mPaint.setAntiAlias(true);
        mPaint.setDither(true);
        mPaint.setColor(Color.GREEN);
        mPaint.setStyle(Paint.Style.STROKE);
        mPaint.setStrokeJoin(Paint.Join.ROUND);
        mPaint.setStrokeCap(Paint.Cap.ROUND);
        mPaint.setStrokeWidth(12);
    }

    public class DrawingView extends View {

        public int width;
        public  int height;
        private Bitmap  mBitmap;
        private Canvas  mCanvas;
        private Canvas  mCanvas1;
        private Canvas  mCanvasT;
        private Path mPath;
        private Paint mBitmapPaint;
        Context context;
        private Paint circlePaint;
        private Path circlePath;

        public DrawingView(Context c) {
            super(c);
            context = c;
            mPath = new Path();
            mBitmapPaint = new Paint(Paint.DITHER_FLAG);
            circlePaint = new Paint();
            circlePath = new Path();
            circlePaint.setAntiAlias(true);
            circlePaint.setColor(Color.BLUE);
            circlePaint.setStyle(Paint.Style.STROKE);
            circlePaint.setStrokeJoin(Paint.Join.MITER);
            circlePaint.setStrokeWidth(4f);
        }

        @Override
        protected void onSizeChanged(int w, int h, int oldw, int oldh) {
            super.onSizeChanged(w, h, oldw, oldh);
            Log.d("YO","onSizeChange");
            mBitmap = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888);
            mCanvas = new Canvas(mBitmap);
            mCanvas1 = new Canvas(mBitmap);
            mCanvasT = new Canvas(mBitmap);
            Paint p = new Paint();
            p.setTextSize(100);
            mCanvasT.drawText("Point Stability Test",20,150,p);
            Log.d("YO",w+","+h);
            int W = mBitmap.getWidth();
            int H = mBitmap.getHeight();
            mCanvas1.drawCircle(W/2,H/2,50,p);
        }

        @Override
        protected void onDraw(Canvas canvas) {
            super.onDraw(canvas);
            canvas.drawBitmap( mBitmap, 0, 0, mBitmapPaint);
            canvas.drawPath( mPath,  mPaint);
            canvas.drawPath( circlePath,  circlePaint);
        }

        private float mX, mY;
        private static final float TOUCH_TOLERANCE = 4;

        private void touch_start(float x, float y) {
            mPath.reset();
            mPath.moveTo(x, y);
            mX = x;
            mY = y;
            float[] f = {x,y,System.currentTimeMillis()};
            list.add(f);
        }

        private void touch_move(float x, float y) {
            float dx = Math.abs(x - mX);
            float dy = Math.abs(y - mY);
            if (dx >= TOUCH_TOLERANCE || dy >= TOUCH_TOLERANCE) {
                mPath.quadTo(mX, mY, (x + mX)/2, (y + mY)/2);
                mX = x;
                mY = y;
                circlePath.reset();
                circlePath.addCircle(mX, mY, 30, Path.Direction.CW);
                float[] f = {x,y,System.currentTimeMillis()};
                list.add(f);
            }
        }

        private void touch_up() {
            mPath.lineTo(mX, mY);
            circlePath.reset();
            // commit the path to our offscreen
            mCanvas.drawPath(mPath,  mPaint);
            // kill this so we don't double draw
            mPath.reset();
            AlertDialog.Builder builder = new AlertDialog.Builder(getContext());
            builder.setMessage("Do you want to submit?")
                    .setTitle("Accept and submit for testing?");
            builder.setPositiveButton("Yes", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
//                    ArrayList<float[]> finalList = new ArrayList<>();
//                    Log.d("qwe",staticDynamicList.size()+"");
//                    Log.d("qwe",list.size()+"");
//                    finalList.addAll(staticDynamicList);
//                    finalList.addAll(list);
//                    Log.d("qwe",finalList.size()+"");
                    submit();
//                    Intent i = new Intent(PointStabilityTest.this,Result.class);
//                    startActivity(i);
//                    dialog.dismiss();
//                    finish();
                }
            });

            builder.setNegativeButton("Retry", new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface dialog, int which) {
                    Intent i = new Intent(PointStabilityTest.this,PointStabilityTest.class);
                    startActivity(i);
                    dialog.dismiss();
                    finish();
                }
            });


            builder.show();
        }

        @Override
        public boolean onTouchEvent(MotionEvent event) {
            float x = event.getX();
            float y = event.getY();

            switch (event.getAction()) {
                case MotionEvent.ACTION_DOWN:
                    touch_start(x, y);
                    invalidate();
                    break;
                case MotionEvent.ACTION_MOVE:
                    touch_move(x, y);
                    invalidate();
                    break;
                case MotionEvent.ACTION_UP:
                    touch_up();
                    invalidate();
                    break;
            }
            return true;
        }
    }

    private void submit() {
        try {
            RequestQueue requestQueue = Volley.newRequestQueue(this);
            String URL = "http://192.168.43.205:5000";
            StringRequest sr = new StringRequest(Request.Method.POST, URL, new Response.Listener<String>() {
                @Override
                public void onResponse(String response) {
                    Log.i("VOLLEY", response);
                    AlertDialog.Builder builder = new AlertDialog.Builder(PointStabilityTest.this);
                    builder.setMessage(response)
                            .setTitle("Results are here!");
                    builder.setPositiveButton("Do-Over", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            Intent i = new Intent(PointStabilityTest.this, MainActivity.class);
                            startActivity(i);
                            dialog.dismiss();
                            finish();
                        }
                    });
                    builder.setPositiveButton("Do-Over", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            Intent i = new Intent(PointStabilityTest.this, MainActivity.class);
                            startActivity(i);
                            dialog.dismiss();
                            finish();
                        }
                    });
                    builder.show();
                }
            }, new Response.ErrorListener() {
                @Override
                public void onErrorResponse(VolleyError error) {
                    Log.e("VOLLEY", error.toString());
                    AlertDialog.Builder builder = new AlertDialog.Builder(PointStabilityTest.this);
                    builder.setMessage("Some error on server. Try again.")
                            .setTitle("Error!");
                    builder.setPositiveButton("Do-Over", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            Intent i = new Intent(PointStabilityTest.this, MainActivity.class);
                            startActivity(i);
                            dialog.dismiss();
                            finish();
                        }
                    });
                    builder.setPositiveButton("Exit", new DialogInterface.OnClickListener() {
                        @Override
                        public void onClick(DialogInterface dialog, int which) {
                            finish();
                        }
                    });
                    builder.show();
                }
            }) {
                @Override
                protected Map<String,String> getParams(){
                    int X = 1080;
                    int Y = 2097;
                    int x = 1400;
                    int y = 800;

                    String data1 = "[";
                    String data2 = "[";
                    String data3 = "[";
                    int n1 = staticList.size();
                    int n2 = dynamicList.size();
                    int n3 = list.size();
                    for(int i=0; i<n1; i++) {
                        data1 += "[";
                        data1 += (staticList.get(i)[0]/X)*x+","+(staticList.get(i)[1]/Y)*y+",0,"+staticList.get(i)[2];
                        if(i==n1-1)
                            data1 += "]";
                        else
                            data1 += "],";
                    }
                    data1 += "]";
                    for(int i=0; i<n2; i++) {
                        data2 += "[";
                        data2 += (dynamicList.get(i)[0]/X)*x+","+(dynamicList.get(i)[1]/Y)*y+",0,"+dynamicList.get(i)[2];
                        if(i==n2-1)
                            data2 += "]";
                        else
                            data2 += "],";
                    }
                    data2 += "]";
                    for(int i=0; i<n2; i++) {
                        data3 += "[";
                        data3 += (dynamicList.get(i)[0]/X)*x+","+(dynamicList.get(i)[1]/Y)*y+",0,"+dynamicList.get(i)[2];
                        if(i==n2-1)
                            data3 += "]";
                        else
                            data3 += "],";
                    }
                    data3 += "]";
                    Map<String,String> params = new HashMap<String, String>();
                    params.put("data1",data1);
                    params.put("data2",data2);
                    params.put("data3",data3);
                    return params;
                }

                @Override
                public Map<String, String> getHeaders() throws AuthFailureError {
                    Map<String,String> params = new HashMap<String, String>();
                    params.put("Content-Type","application/x-www-form-urlencoded");
                    return params;
                }
            };

            requestQueue.add(sr);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
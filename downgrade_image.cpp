#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace std;
using namespace cv;

Mat& color_space_reduction(Mat& i, const uchar* const table);

int main()
{
    Mat I;
    string filename = "lenna.png";
    I = imread(filename, IMREAD_COLOR);

    if (!I.data)
    {
        cout << "img cannot be loaded";
        return -1;
    }
    
    int dividenum;
    cin >> dividenum;

    uchar table[256];
    for (int i = 0; i < 256; i++)
        table[i] = (uchar)dividenum * (i / dividenum);

    double t = (double)getTickCount();

    color_space_reduction(I, table);

    imwrite("output.png", I);

    t = (getTickCount() - t) / getTickFrequency();
    cout << "The required time is: " << t << endl;
    
    return 0;
}

Mat& color_space_reduction(Mat& i, const uchar* const table)
{
    CV_Assert(i.depth() == CV_8U);

    int channels = i.channels();
    int nRows = i.rows;
    int nCols = i.cols * channels;

    if (i.isContinuous())
    {
        nCols *= nRows;
        nRows = 1;
    }
    
    uchar* p = i.data;
    for (int i = 0; i < nRows*nCols; i++)
    {
        *p++ = table[*p];
    }
    
    return i;
}

#include <iostream>
#include <string>
#include <sstream>
#include <cstring>
#include <iomanip>

//rotating macro
#define rotateleft(x,n) ((x<<n) | (x>>(32-n)))
#define rotateright(x,n) ((x>>n) | (x<<(32-n)))

//converts to hex string representation
template< typename T >
std::string int_to_hex( T i )
{
    std::stringstream stream;
    stream << std::setfill('0') << std::setw(sizeof(T)*2)
           << std::hex << i;
    return stream.str();
}

//converts message to it's SHA-1 hash
std::string getSHA1Hash(unsigned char* message)
{
    unsigned long h0, h1, h2, h3, h4, a, b, c, d, e, f, k, temp; //4 bytes = 32 bits
    int i;

    //constants initialization
    h0 = 0x67452301;
    h1 = 0xEFCDAB89;
    h2 = 0x98BADCFE;
    h3 = 0x10325476;
    h4 = 0xC3D2E1F0;

    unsigned char* str;
    str = (unsigned char *)malloc(strlen((const char *)message)+100);
    strcpy((char*)str, (const char*) message);

    int cur_len = strlen((const char*) str);
    int orig_len = cur_len;
    str[cur_len] = 0x80;
    str[cur_len + 1] = '\0';

    cur_len++;

    int ib = cur_len % 64;
    if(ib < 56) ib = 56 - ib;
    else ib = 120 - ib;

    for(i = 0; i < ib; i++)
    {
        str[cur_len] = 0x00;
        cur_len++;
    }
    str[cur_len + 1] = '\0';

    for(i = 0; i < 6; i++)
    {
        str[cur_len]=0x0;
        cur_len++;
    }

    str[cur_len] = (orig_len * 8) / 0x100;
    cur_len++;
    str[cur_len] = (orig_len * 8) % 0x100;
    cur_len++;
    str[cur_len + i] = '\0';

    int number_of_chunks = cur_len/64;
    unsigned long int word[80];

    for(i = 0; i < number_of_chunks; i++)
    {
        for(int j=0;j<16;j++)
        {
            word[j] = str[i*64 + j*4 + 0] * 0x1000000 + str[i*64 + j*4 + 1] * 0x10000 + str[i*64 + j*4 + 2] * 0x100 + str[i*64 + j*4 + 3];
        }
        for(int j=16;j<80;j++)
        {
            word[j] = rotateleft((word[j-3] ^ word[j-8] ^ word[j-14] ^ word[j-16]),1);
        }

        a = h0;
        b = h1;
        c = h2;
        d = h3;
        e = h4;

        for(int m=0;m<80;m++)
        {
            if(m<=19)
            {
                f = (b & c) | ((~b) & d);
                k = 0x5A827999;
            }
            else if(m<=39)
            {
                f = b ^ c ^ d;
                k = 0x6ED9EBA1;
            }
            else if(m<=59)
            {
                f = (b & c) | (b & d) | (c & d);
                k = 0x8F1BBCDC;
            }
            else
            {
                f = b ^ c ^ d;
                k = 0xCA62C1D6;
            }

            temp = (rotateleft(a,5) + f + e + k + word[m]) & 0xFFFFFFFF;
            e = d;
            d = c;
            c = rotateleft(b,30);
            b = a;
            a = temp;

        }

        h0 = h0 + a;
        h1 = h1 + b;
        h2 = h2 + c;
        h3 = h3 + d;
        h4 = h4 + e;

    }

    return int_to_hex(h0)+ int_to_hex(h1)+ int_to_hex(h2)+ int_to_hex(h3)+ int_to_hex(h4);
}

//Prints a test case
void print_case(const char* message)
{
    std::cout << "Message : " << message << "\n\tHash :" << getSHA1Hash((unsigned char*)message) << '\n';
}

int main()
{
    std::cout << "Test Vectors :" << std::endl;
    print_case("abc");
    print_case("abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq");
    print_case("0");

    return 0;
}

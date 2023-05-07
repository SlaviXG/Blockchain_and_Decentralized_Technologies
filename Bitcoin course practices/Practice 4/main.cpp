#include <iostream>

/**
    Vigenère Cipher
*/

using namespace std;

// Encryption
string get_encryption(string plain_text, string key)
{
    string cipher_text;

    for (int i = 0; i < plain_text.size(); i++)
    {
        char x = (plain_text[i] + key[i]) % 26 + 'A';
        cipher_text.push_back(x);
    }

    return cipher_text;
}

// Decryption
string get_decryption(string cipher_text, string key)
{
    string plain_text;

    for (int i = 0 ; i < cipher_text.size(); i++)
    {
        char x = (cipher_text[i] - key[i] + 26) %26 + 'A';
        plain_text.push_back(x);
    }

    return plain_text;
}

// Generate Key
// the function cycles the key
string generate_key(string plain_text, string key)
{
    for(int i = 0; key.size() != plain_text.size(); i++)
    {
        if(i == plain_text.size()) i = 0;
        key.push_back(key[i]);
    }

    return key;
}

int main()
{
    string str = "ABACABATHETEXT";
    string keyword = "THEKEY";

    string key = generate_key(str, keyword);
    string encrypted_text = get_encryption(str, key);

    cout << "Encrypted text: " << encrypted_text << endl;
    cout << "Original text: " << get_decryption(encrypted_text, key) << endl;

    return 0;
}

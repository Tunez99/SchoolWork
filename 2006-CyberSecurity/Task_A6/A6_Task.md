A6 Discover cryptographic implementation used offline.

https://www.trentonsystems.com/en-us/resource-hub/blog/what-is-intel-tme

https://www.intel.com/content/www/us/en/developer/articles/news/runtime-encryption-of-memory-with-intel-tme-mk.html

With the emergence of memory based attacks, security measures have implemented to counter this.

Such attacks could include:
Cold boot attacks
Physical attacks
Kernel Mapping attacks
Freed Data leak attacks

In response, the Intel TME (Total Memory Encryption) was developing. It works by encrypting all data passing to and from the computers CPU. 

While online, data is encrypted using various methods (SSL/TLS/HTTPS), the CPU processes the same data not protected using cryptology. 

One issue, is that in a full disk encryption, sectors are chained with an IV (initialisation vector). However AES-XTS allows access to sectors independently, wihtout compromising security.

Intel TME works to encrypt the entire physical memory with a single encryption key. It encrypts memory sectors and external memory buses with a NIST Standard AES-XTS algorithm with 128- bits.

----- USING AES-XTS
https://asecuritysite.com/symmetric/xts

We can gather from this site an insight into how the encryption works. (See AES-XTS for a mathematical overview.)

We can see that 2 keys are defined, one handles the encryption while the other one creates a "tweak" based on the location in memory. 

This ensures that each blocks of data can be decrypted independently, allowing flexible memory encryption.



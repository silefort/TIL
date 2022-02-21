# Check a .cer Certificate File

    openssl crl2pkcs7 -nocrl -certfile fork_interm.cer | openssl pkcs7 -print_certs -noout -text | grep -e "Subject:\|Not After" | awk -F',' '{ print $NF }'

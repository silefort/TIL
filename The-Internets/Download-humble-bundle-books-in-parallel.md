# Download all of humble bundle books in parallel

Open the Developer Tools while on the download page and paste the following:

    var pattern = /(MOBI|EPUB|PDF( ?\(H.\))?|CBZ|Download)$/i;
    var nodes = document.getElementsByTagName('a');
    var downloadCmd = '';
    for (i in nodes) {
        var a = nodes[i];
        if (a && a.text && pattern.test(a.text.trim()) && a.attributes['data-web']) {
            downloadCmd += 'wget --content-disposition "' + a.attributes['data-web'].value + "\"\n";
        }
    }
    var output = document.createElement("pre");
    output.textContent = downloadCmd;
    document.getElementById("papers-content").prepend(output);


This will add a pre tag to the page with a bunch of wget commands. Go ahead and copy those to your clipboard.

    parallel -j 4 < download_jobs

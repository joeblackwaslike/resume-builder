FROM debian:stretch

# Stretch is the last Debian version with texlive 2016 but it's sources were moved to archive.debian.org
# and stretch updates has been deprecated.  We need to update the sources list to point to the archive.
COPY sources.list /etc/apt/

RUN apt-get update && \
        apt-get install -y \
            wget \
            xzdec \
            cm-super \
            texlive \
            texlive-xetex \
            texlive-fonts-extra \
            texinfo \
            && \
        apt-get clean && \
        rm -rf /var/lib/apt/*
    
RUN mkdir /root/tetxf
RUN tlmgr init-usertree
# RUN tlmgr --usermode install ucharcat
RUN apt-get update && \
    apt-get install -y \
        texlive-luatex

VOLUME ["/mnt/system"]

WORKDIR /mnt/system

CMD ["/usr/bin/xelatex"]

#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-ecodist
Version  : 2.0.1
Release  : 16
URL      : https://cran.r-project.org/src/contrib/ecodist_2.0.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/ecodist_2.0.1.tar.gz
Summary  : Dissimilarity-Based Functions for Ecological Analysis
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-ecodist-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
ecodist R package

%package lib
Summary: lib components for the R-ecodist package.
Group: Libraries

%description lib
lib components for the R-ecodist package.


%prep
%setup -q -c -n ecodist

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571822370

%install
export SOURCE_DATE_EPOCH=1571822370
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ecodist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ecodist
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library ecodist
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc ecodist || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/ecodist/CITATION
/usr/lib64/R/library/ecodist/DESCRIPTION
/usr/lib64/R/library/ecodist/INDEX
/usr/lib64/R/library/ecodist/Meta/Rd.rds
/usr/lib64/R/library/ecodist/Meta/data.rds
/usr/lib64/R/library/ecodist/Meta/features.rds
/usr/lib64/R/library/ecodist/Meta/hsearch.rds
/usr/lib64/R/library/ecodist/Meta/links.rds
/usr/lib64/R/library/ecodist/Meta/nsInfo.rds
/usr/lib64/R/library/ecodist/Meta/package.rds
/usr/lib64/R/library/ecodist/Meta/vignette.rds
/usr/lib64/R/library/ecodist/NAMESPACE
/usr/lib64/R/library/ecodist/R/ecodist
/usr/lib64/R/library/ecodist/R/ecodist.rdb
/usr/lib64/R/library/ecodist/R/ecodist.rdx
/usr/lib64/R/library/ecodist/data/Rdata.rdb
/usr/lib64/R/library/ecodist/data/Rdata.rds
/usr/lib64/R/library/ecodist/data/Rdata.rdx
/usr/lib64/R/library/ecodist/doc/dissimilarity.Rmd
/usr/lib64/R/library/ecodist/doc/dissimilarity.html
/usr/lib64/R/library/ecodist/doc/index.html
/usr/lib64/R/library/ecodist/help/AnIndex
/usr/lib64/R/library/ecodist/help/aliases.rds
/usr/lib64/R/library/ecodist/help/ecodist.rdb
/usr/lib64/R/library/ecodist/help/ecodist.rdx
/usr/lib64/R/library/ecodist/help/paths.rds
/usr/lib64/R/library/ecodist/html/00Index.html
/usr/lib64/R/library/ecodist/html/R.css
/usr/lib64/R/library/ecodist/tests/testthat.R
/usr/lib64/R/library/ecodist/tests/testthat/test-MRM.R
/usr/lib64/R/library/ecodist/tests/testthat/test-crosstab.R
/usr/lib64/R/library/ecodist/tests/testthat/test-distance.R
/usr/lib64/R/library/ecodist/tests/testthat/test-mantel.R
/usr/lib64/R/library/ecodist/tests/testthat/test-mgroup.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/ecodist/libs/ecodist.so
/usr/lib64/R/library/ecodist/libs/ecodist.so.avx2
/usr/lib64/R/library/ecodist/libs/ecodist.so.avx512

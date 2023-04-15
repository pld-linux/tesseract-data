%define		tesseract_ver	4.0.0

Summary:	Trained data for Tesseract Open Source OCR Engine
Summary(pl.UTF-8):	Wytrenowane dane dla Tesseracta - silnika OCR o otwartych źródłach
Name:		tesseract-data
Version:	4.1.0
Release:	1
License:	Apache v2.0
Group:		Applications/Graphics
#Source0Download: https://github.com/tesseract-ocr/tessdata/releases
Source0:	https://github.com/tesseract-ocr/tessdata/archive/%{version}/tessdata-%{version}.tar.gz
# Source0-md5:	89e25c7c40a59be7195422a01f57fcb2
# from tessdata-4.00/kur.traineddata (Arabic version of kur data, dropped in 4.1)
Source10:	kur.traineddata
# Source10-md5:	e6d3776d097e008a9e965aa373a9ea29
URL:		https://github.com/tesseract-ocr/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trained data for Tesseract Open Source OCR Engine.

%description -l pl.UTF-8
Wytrenowane dane dla Tesseracta - silnika OCR o otwartych źródłach.

%package equ
Summary:	Mathematical equations recognition data for Tesseract
Summary(pl.UTF-8):	Dane dla Tesseracta pozwalające na rozpoznawanie równań matematycznych
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description equ
Mathematical equations recognition data for Tesseract.

%description equ -l pl.UTF-8
Dane dla Tesseracta pozwalające na rozpoznawanie równań
matematycznych.

%package osd
Summary:	Orientation and script detection data for Tesseract
Summary(pl.UTF-8):	Dane dla Tesseracta pozwalające na wykrywanie orientacji i pisma
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description osd
Orientation and script detection data for Tesseract.

%description osd -l pl.UTF-8
Dane dla Tesseracta pozwalające na wykrywanie orientacji i pisma.

%package lang-af
Summary:	Afrikaans language data for Tesseract
Summary(pl.UTF-8):	Dane języka afrykanerskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-af
This package contains the data files required to recognize Afrikaans
language.

%description lang-af -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
afrykanerskiego.

%package lang-am
Summary:	Amharic language data for Tesseract
Summary(pl.UTF-8):	Dane języka amharskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-am
This package contains the data files required to recognize Amharic
language.

%description lang-am -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
amharskiego.

%package lang-ar
Summary:	Arabic language data for Tesseract
Summary(pl.UTF-8):	Dane języka arabskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-ar

%description lang-ar
This package contains the data files required to recognize Arabic
language.

%description lang-ar -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
arabskiego.

%package lang-as
Summary:	Assamese language data for Tesseract
Summary(pl.UTF-8):	Dane języka asamskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-as
This package contains the data files required to recognize Assamese
language.

%description lang-as -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
asamskiego.

%package lang-az
Summary:	Azerbaijani language data for Tesseract
Summary(pl.UTF-8):	Dane języka azerskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-az
This package contains the data files required to recognize Azerbaijani
language.

%description lang-az -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
azerskiego.

%package lang-be
Summary:	Belarusian language data for Tesseract
Summary(pl.UTF-8):	Dane języka białoruskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-be
This package contains the data files required to recognize Belarusian
language.

%description lang-be -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
białoruskiego.

%package lang-bn
Summary:	Bengali language data for Tesseract
Summary(pl.UTF-8):	Dane języka bengalskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-bn
This package contains the data files required to recognize Bengali
language.

%description lang-bn -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
bengalskiego.

%package lang-bo
Summary:	Tibetan language data for Tesseract
Summary(pl.UTF-8):	Dane języka tybetańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-bo
This package contains the data files required to recognize Tibetan
language.

%description lang-bo -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tybetańskiego.

%package lang-bs
Summary:	Bosnian language data for Tesseract
Summary(pl.UTF-8):	Dane języka bośniackiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-bs
This package contains the data files required to recognize Bosnian
language.

%description lang-bs -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
bośniackiego.

%package lang-br
Summary:	Breton language data for Tesseract
Summary(pl.UTF-8):	Dane języka bretońskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-br
This package contains the data files required to recognize Breton
language.

%description lang-br -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
bretońskiego.

%package lang-bg
Summary:	Bulgarian language data for Tesseract
Summary(pl.UTF-8):	Dane języka bułgarskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-bg

%description lang-bg
This package contains the data files required to recognize Bulgarian
language.

%description lang-bg -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
bułgarskiego.

%package lang-ca
Summary:	Catalan language data for Tesseract
Summary(pl.UTF-8):	Dane języka katalońskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= 3.00
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-ca

%description lang-ca
This package contains the data files required to recognize Catalan
language.

%description lang-ca -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
katalońskiego.

%package lang-ceb
Summary:	Cebuano language data for Tesseract
Summary(pl.UTF-8):	Dane języka cebuańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ceb
This package contains the data files required to recognize Cebuano
language.

%description lang-ceb -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
cebuańskiego.

%package lang-cs
Summary:	Czech language data for Tesseract
Summary(pl.UTF-8):	Dane języka czeskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-cs

%description lang-cs
This package contains the data files required to recognize Czech
language.

%description lang-cs -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
czeskiego.

%package lang-zh_CN
Summary:	Chinese Simplified language data for Tesseract
Summary(pl.UTF-8):	Dane języka chińskiego uproszczonego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-zh_CN

%description lang-zh_CN
This package contains the data files required to recognize Chinese
Simplified language.

%description lang-zh_CN -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
chińskiego uproszczonego.

%package lang-zh_TW
Summary:	Chinese Traditional language data for Tesseract
Summary(pl.UTF-8):	Dane języka chińskiego tradycyjnego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-zh_TW

%description lang-zh_TW
This package contains the data files required to recognize Chinese
Traditional language.

%description lang-zh_TW -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
chińskiego tradycyjnego.

%package lang-chr
Summary:	Cherokee language data for Tesseract
Summary(pl.UTF-8):	Dane języka czerokeskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-chr

%description lang-chr
This package contains the data files required to recognize Cherokee
language.

%description lang-chr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
czerokeskiego.

%package lang-co
Summary:	Corsican language data for Tesseract
Summary(pl.UTF-8):	Dane języka korsykańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-co
This package contains the data files required to recognize Corsican
language.

%description lang-co -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
korsykańskiego.

%package lang-cy
Summary:	Welsh language data for Tesseract
Summary(pl.UTF-8):	Dane języka walijskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-cy
This package contains the data files required to recognize Welsh
language.

%description lang-cy -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
walijskiego.

%package lang-da
Summary:	Danish language data for Tesseract
Summary(pl.UTF-8):	Dane języka duńskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-da

%description lang-da
This package contains the data files required to recognize Danish
language (including Fraktur).

%description lang-da -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
duńskiego (także pisanego frakturą).

%package lang-de
Summary:	German language data for Tesseract
Summary(pl.UTF-8):	Dane języka niemieckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-deu < 2.00-1
Obsoletes:	tesseract-lang-de < 3
Obsoletes:	tesseract-lang-deu < 2.01

%description lang-de
This package contains the data files required to recognize German
language (including Fraktur).

%description lang-de -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
niemieckiego (także pisanego frakturą).

%package lang-dv
Summary:	Divehi language data for Tesseract
Summary(pl.UTF-8):	Dane języka divehi (malediwskiego) dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-dv
This package contains the data files required to recognize Divehi
language.

%description lang-dv -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
divehi (malediwskiego).

%package lang-dz
Summary:	Dzongkha language data for Tesseract
Summary(pl.UTF-8):	Dane języka dzongka dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-dz
This package contains the data files required to recognize Dzongkha
language.

%description lang-dz -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
dzongka.

%package lang-el
Summary:	Greek language data for Tesseract
Summary(pl.UTF-8):	Dane języka greckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-el

%description lang-el
This package contains the data files required to recognize Greek
language.

%description lang-el -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
greckiego.

%package lang-en
Summary:	English language data for Tesseract
Summary(pl.UTF-8):	Dane języka angielskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-eng < 2.00-1
Obsoletes:	tesseract-lang-en < 3
Obsoletes:	tesseract-lang-eng < 2.01

%description lang-en
This package contains the data files required to recognize English
language.

%description lang-en -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
angielskiego.

%package lang-enm
Summary:	Middle English language data for Tesseract
Summary(pl.UTF-8):	Dane języka angielskiego średniowiecznego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-enm
This package contains the data files required to recognize Middle
English language.

%description lang-enm -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
angielskiego średniowiecznego.

%package lang-eo
Summary:	Esperanto language data for Tesseract
Summary(pl.UTF-8):	Dane języka esperanto dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-eo
This package contains the data files required to recognize Esperanto
language.

%description lang-eo -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
esperanto.

%package lang-et
Summary:	Estonian language data for Tesseract
Summary(pl.UTF-8):	Dane języka estońskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-et
This package contains the data files required to recognize Estonian
language.

%description lang-et -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
estońskiego.

%package lang-eu
Summary:	Basque language data for Tesseract
Summary(pl.UTF-8):	Dane języka baskijkiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-eu
This package contains the data files required to recognize Basque
language.

%description lang-eu -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
baskijkiego.

%package lang-fo
Summary:	Faroese language data for Tesseract
Summary(pl.UTF-8):	Dane języka farerskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-fo
This package contains the data files required to recognize Faroese
language.

%description lang-fo -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
farerskiego.

%package lang-fa
Summary:	Persian language data for Tesseract
Summary(pl.UTF-8):	Dane języka perskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-fa
This package contains the data files required to recognize Persian
language.

%description lang-fa -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
perskiego.

%package lang-fil
Summary:	Filipino language data for Tesseract
Summary(pl.UTF-8):	Dane języka pilipino dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-fil
This package contains the data files required to recognize Filipino
language.

%description lang-fil -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
pilipino.

%package lang-fi
Summary:	Finnish language data for Tesseract
Summary(pl.UTF-8):	Dane języka fińskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-fi

%description lang-fi
This package contains the data files required to recognize Finnish
language.

%description lang-fi -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
fińskiego.

%package lang-fr
Summary:	French language data for Tesseract
Summary(pl.UTF-8):	Dane języka francuskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-fra < 2.00-1
Obsoletes:	tesseract-lang-fr < 3
Obsoletes:	tesseract-lang-fra < 2.01

%description lang-fr
This package contains the data files required to recognize French
language.

%description lang-fr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
francuskiego.

%package lang-frk
Summary:	Frankish language data for Tesseract
Summary(pl.UTF-8):	Dane języka frankijskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-frk
This package contains the data files required to recognize Frankish
language.

%description lang-frk -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
frankijskiego.

%package lang-frm
Summary:	Middle French language data for Tesseract
Summary(pl.UTF-8):	Dane języka francuskiego średniowiecznego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-frm
This package contains the data files required to recognize Middle
French language.

%description lang-frm -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
francuskiego średniowiecznego.

%package lang-fy
Summary:	Frisian language data for Tesseract
Summary(pl.UTF-8):	Dane języka fryzyjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-fy
This package contains the data files required to recognize Frisian
language.

%description lang-fy -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
fryzyjskiego.

%package lang-gd
Summary:	Gaelic language data for Tesseract
Summary(pl.UTF-8):	Dane języka szkockiego gaelickiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-gd
This package contains the data files required to recognize Gaelic
language.

%description lang-gd -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
szkockiego gaelickiego.

%package lang-ga
Summary:	Irish language data for Tesseract
Summary(pl.UTF-8):	Dane języka irlandzkiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ga
This package contains the data files required to recognize Irish
language.

%description lang-ga -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
irlandzkiego.

%package lang-gl
Summary:	Galician language data for Tesseract
Summary(pl.UTF-8):	Dane języka galicyjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-gl
This package contains the data files required to recognize Galician
language.

%description lang-gl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
galicyjskiego.

%package lang-grc
Summary:	Ancient Greek language data for Tesseract
Summary(pl.UTF-8):	Dane języka greckiego starożytnego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-grc
This package contains the data files required to recognize Ancient
Greek language.

%description lang-grc -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
greckiego starożytnego.

%package lang-gu
Summary:	Gujarati language data for Tesseract
Summary(pl.UTF-8):	Dane języka gudźarati dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-gu
This package contains the data files required to recognize Gujarati
language.

%description lang-gu -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
gudźarati.

%package lang-ht
Summary:	Haitian language data for Tesseract
Summary(pl.UTF-8):	Dane języka haitańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ht
This package contains the data files required to recognize Haitian
language.

%description lang-ht -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
haitańskiego.

%package lang-he
Summary:	Hebrew language data for Tesseract
Summary(pl.UTF-8):	Dane języka hebrajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-he
This package contains the data files required to recognize Hebrew
language.

%description lang-he -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
hebrajskiego.

%package lang-hi
Summary:	Hindi language data for Tesseract
Summary(pl.UTF-8):	Dane języka hindi dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-hi

%description lang-hi
This package contains the data files required to recognize Hindi
language.

%description lang-hi -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
hindi.

%package lang-hr
Summary:	Croatian language data for Tesseract
Summary(pl.UTF-8):	Dane języka chorwackiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-hr
This package contains the data files required to recognize Croatian
language.

%description lang-hr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
chorwackiego.

%package lang-hu
Summary:	Hungarian language data for Tesseract
Summary(pl.UTF-8):	Dane języka węgierskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-hu

%description lang-hu
This package contains the data files required to recognize Hungarian
language.

%description lang-hu -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
węgierskiego.

%package lang-hy
Summary:	Armenian language data for Tesseract
Summary(pl.UTF-8):	Dane języka ormiańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-hy
This package contains the data files required to recognize Armenian
language.

%description lang-hy -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
ormiańskiego.

%package lang-iu
Summary:	Inuktitut language data for Tesseract
Summary(pl.UTF-8):	Dane języka inuktitut dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-iu
This package contains the data files required to recognize Inuktitut
language.

%description lang-iu -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
inuktitut.

%package lang-id
Summary:	Indonesian language data for Tesseract
Summary(pl.UTF-8):	Dane języka indonezyjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-id

%description lang-id
This package contains the data files required to recognize Indonesian
language.

%description lang-id -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
indonezyjskiego.

%package lang-is
Summary:	Icelandic language data for Tesseract
Summary(pl.UTF-8):	Dane języka islandzkiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-is
This package contains the data files required to recognize Icelandic
language.

%description lang-is -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
islandzkiego.

%package lang-it
Summary:	Italian language data for Tesseract
Summary(pl.UTF-8):	Dane języka włoskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= 3.00
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-ita < 2.00-1
Obsoletes:	tesseract-lang-it < 3
Obsoletes:	tesseract-lang-ita < 2.01

%description lang-it
This package contains the data files required to recognize Italian
language.

%description lang-it -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
włoskiego.

%package lang-jv
Summary:	Javanese language data for Tesseract
Summary(pl.UTF-8):	Dane języka jawajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-jv
This package contains the data files required to recognize Javanese
language.

%description lang-jv -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
jawajskiego.

%package lang-ja
Summary:	Japanese language data for Tesseract
Summary(pl.UTF-8):	Dane języka japońskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-ja

%description lang-ja
This package contains the data files required to recognize Japanese
language.

%description lang-ja -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
japońskiego.

%package lang-kn
Summary:	Kannada language data for Tesseract
Summary(pl.UTF-8):	Dane języka kannada dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-kn
This package contains the data files required to recognize Kannada
language.

%description lang-kn -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
kannada.

%package lang-ka
Summary:	Georgian language data for Tesseract
Summary(pl.UTF-8):	Dane języka gruzińskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ka
This package contains the data files required to recognize Georgian
language.

%description lang-ka -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
gruzińskiego.

%package lang-kk
Summary:	Kazakh language data for Tesseract
Summary(pl.UTF-8):	Dane języka kazaskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-kk
This package contains the data files required to recognize Kazakh
language.

%description lang-kk -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
kazaskiego.

%package lang-km
Summary:	Kkmer language data for Tesseract
Summary(pl.UTF-8):	Dane języka khmerskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-km
This package contains the data files required to recognize Kkmer
language.

%description lang-km -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
khmerskiego.

%package lang-ky
Summary:	Kirghiz language data for Tesseract
Summary(pl.UTF-8):	Dane języka kirgiskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ky
This package contains the data files required to recognize Kirghiz
language.

%description lang-ky -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
kirgiskiego.

%package lang-kmr
Summary:	Kurmanji (Northern Kurdish) language data for Tesseract
Summary(pl.UTF-8):	Dane języka kurmandżi (północnokurdyjskiego) dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-kmr
This package contains the data files required to recognize Kurmanji
(Northern Kurdish) language.

%description lang-kmr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
kurmandżi (północnokurdyjskiego).

%package lang-ko
Summary:	Korean language data for Tesseract
Summary(pl.UTF-8):	Dane języka koreańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-ko

%description lang-ko
This package contains the data files required to recognize Korean
language.

%description lang-ko -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
koreańskiego.

%package lang-ku
Summary:	Kurdish language data for Tesseract
Summary(pl.UTF-8):	Dane języka kurdyjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ku
This package contains the data files required to recognize Kurdish
language.

%description lang-ku -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
kurdyjskiego.

%package lang-lo
Summary:	Lao language data for Tesseract
Summary(pl.UTF-8):	Dane języka laotańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-lo
This package contains the data files required to recognize Lao
language.

%description lang-lo -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
laotańskiego.

%package lang-la
Summary:	Latin language data for Tesseract
Summary(pl.UTF-8):	Dane języka łacińskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-la
This package contains the data files required to recognize Latin
language.

%description lang-la -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
łacińskiego.

%package lang-lv
Summary:	Latvian language data for Tesseract
Summary(pl.UTF-8):	Dane języka łotewskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-lv

%description lang-lv
This package contains the data files required to recognize Latvian
language.

%description lang-lv -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
łotewskiego.

%package lang-lt
Summary:	Lithuanian language data for Tesseract
Summary(pl.UTF-8):	Dane języka litewskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-lt

%description lang-lt
This package contains the data files required to recognize Lithuanian
language.

%description lang-lt -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
litewskiego.

%package lang-lb
Summary:	Luxembourgish language data for Tesseract
Summary(pl.UTF-8):	Dane języka luksemburskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-lb
This package contains the data files required to recognize
Luxembourgish language.

%description lang-lb -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
luksemburskiego.

%package lang-ml
Summary:	Malayalam language data for Tesseract
Summary(pl.UTF-8):	Dane języka malajalam dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ml
This package contains the data files required to recognize Malayalam
language.

%description lang-ml -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
malajalam.

%package lang-mr
Summary:	Marathi language data for Tesseract
Summary(pl.UTF-8):	Dane języka marathi dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-mr
This package contains the data files required to recognize Marathi
language.

%description lang-mr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
marathi.

%package lang-mk
Summary:	Macedonian language data for Tesseract
Summary(pl.UTF-8):	Dane języka macedońskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-mk
This package contains the data files required to recognize Macedonian
language.

%description lang-mk -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
macedońskiego.

%package lang-mt
Summary:	Maltese language data for Tesseract
Summary(pl.UTF-8):	Dane języka maltańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-mt
This package contains the data files required to recognize Maltese
language.

%description lang-mt -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
maltańskiego.

%package lang-mn
Summary:	Mongolian language data for Tesseract
Summary(pl.UTF-8):	Dane języka mongolskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-mn
This package contains the data files required to recognize Mongolian
language.

%description lang-mn -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
mongolskiego.

%package lang-mi
Summary:	Maori language data for Tesseract
Summary(pl.UTF-8):	Dane języka maoryskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-mi
This package contains the data files required to recognize Maori
language.

%description lang-mi -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
maoryskiego.

%package lang-ms
Summary:	Malay language data for Tesseract
Summary(pl.UTF-8):	Dane języka malajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ms
This package contains the data files required to recognize Malay
language.

%description lang-ms -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
malajskiego.

%package lang-my
Summary:	Burmese language data for Tesseract
Summary(pl.UTF-8):	Dane języka birmańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-my
This package contains the data files required to recognize Burmese
language.

%description lang-my -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
birmańskiego.

%package lang-ne
Summary:	Nepali language data for Tesseract
Summary(pl.UTF-8):	Dane języka nepalskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ne
This package contains the data files required to recognize Nepali
language.

%description lang-ne -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
nepalskiego.

%package lang-nl
Summary:	Dutch language data for Tesseract
Summary(pl.UTF-8):	Dane języka holenderskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-nld < 2.00-1
Obsoletes:	tesseract-lang-nl < 3
Obsoletes:	tesseract-lang-nld < 2.01

%description lang-nl
This package contains the data files required to recognize Dutch
language.

%description lang-nl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
holenderskiego.

%package lang-nb
Summary:	Norwegian language data for Tesseract
Summary(pl.UTF-8):	Dane języka norweskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-nb

%description lang-nb
This package contains the data files required to recognize Norwegian
language.

%description lang-nb -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
norweskiego.

%package lang-oc
Summary:	Occitan language data for Tesseract
Summary(pl.UTF-8):	Dane języka okcytańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-oc
This package contains the data files required to recognize Occitan
language.

%description lang-oc -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
okcytańskiego.

%package lang-or
Summary:	Oriya language data for Tesseract
Summary(pl.UTF-8):	Dane języka orija dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-or
This package contains the data files required to recognize Oriya
language.

%description lang-or -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
orija.

%package lang-pa
Summary:	Panjabi language data for Tesseract
Summary(pl.UTF-8):	Dane języka pendżabskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-pa
This package contains the data files required to recognize Panjabi
language.

%description lang-pa -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
pendżabskiego.

%package lang-pl
Summary:	Polish language data for Tesseract
Summary(pl.UTF-8):	Dane języka polskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-pl
Obsoletes:	tesseract-polish < 0.1

%description lang-pl
This package contains the data files required to recognize Polish
language.

%description lang-pl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
polskiego.

%package lang-pt
Summary:	Portuguese language data for Tesseract
Summary(pl.UTF-8):	Dane języka portugalskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-pt

%description lang-pt
This package contains the data files required to recognize Portuguese
language.

%description lang-pt -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
portugalskiego.

%package lang-ps
Summary:	Pushto language data for Tesseract
Summary(pl.UTF-8):	Dane języka paszto dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ps
This package contains the data files required to recognize Pushto
language.

%description lang-ps -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
paszto.

%package lang-qu
Summary:	Quechua language data for Tesseract
Summary(pl.UTF-8):	Dane języka keczua dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-qu
This package contains the data files required to recognize Quechua
language.

%description lang-qu -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
keczua.

%package lang-ro
Summary:	Romanian language data for Tesseract
Summary(pl.UTF-8):	Dane języka rumuńskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-ro

%description lang-ro
This package contains the data files required to recognize Romanian
language.

%description lang-ro -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
rumuńskiego.

%package lang-ru
Summary:	Russian language data for Tesseract
Summary(pl.UTF-8):	Dane języka rosyjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-ru

%description lang-ru
This package contains the data files required to recognize Russian
language.

%description lang-ru -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
rosyjskiego.

%package lang-sa
Summary:	Sanskrit language data for Tesseract
Summary(pl.UTF-8):	Dane sanskrytu dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-sa
This package contains the data files required to recognize Sanskrit
language.

%description lang-sa -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania sanskrytu.

%package lang-si
Summary:	Sinhala language data for Tesseract
Summary(pl.UTF-8):	Dane języka syngaleskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-si
This package contains the data files required to recognize Sinhala
language.

%description lang-si -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
syngaleskiego.

%package lang-sk
Summary:	Slovakian language data for Tesseract
Summary(pl.UTF-8):	Dane języka słowackiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-sk

%description lang-sk
This package contains the data files required to recognize Slovakian
language (including Fraktur).

%description lang-sk -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
słowackiego (także pisanego frakturą).

%package lang-sl
Summary:	Slovenian language data for Tesseract
Summary(pl.UTF-8):	Dane języka słoweńskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-sl

%description lang-sl
This package contains the data files required to recognize Slovenian
language.

%description lang-sl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
słoweńskiego.

%package lang-sd
Summary:	Sindhi language data for Tesseract
Summary(pl.UTF-8):	Dane języka sindhi dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-sd
This package contains the data files required to recognize Sindhi
language.

%description lang-sd -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
sindhi.

%package lang-es
Summary:	Spanish language data for Tesseract
Summary(pl.UTF-8):	Dane języka hiszpańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-spa < 2.00-1
Obsoletes:	tesseract-lang-es < 3
Obsoletes:	tesseract-lang-spa < 2.01

%description lang-es
This package contains the data files required to recognize Spanish
language.

%description lang-es -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
hiszpańskiego.

%package lang-sq
Summary:	Albanian language data for Tesseract
Summary(pl.UTF-8):	Dane języka albańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-sq
This package contains the data files required to recognize Albanian
language.

%description lang-sq -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
albańskiego.

%package lang-sr
Summary:	Serbian language data for Tesseract
Summary(pl.UTF-8):	Dane języka serbskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-sr

%description lang-sr
This package contains the data files required to recognize Serbian
language.

%description lang-sr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
serbskiego.

%package lang-su
Summary:	Sundanese language data for Tesseract
Summary(pl.UTF-8):	Dane języka sundajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-su
This package contains the data files required to recognize Sundanese
language.

%description lang-su -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
sundajskiego.

%package lang-sw
Summary:	Swahili language data for Tesseract
Summary(pl.UTF-8):	Dane języka suahili dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-sw
This package contains the data files required to recognize Swahili
language.

%description lang-sw -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
suahili.

%package lang-sv
Summary:	Swedish language data for Tesseract
Summary(pl.UTF-8):	Dane języka szwedzkiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-sv

%description lang-sv
This package contains the data files required to recognize Swedish
language.

%description lang-sv -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
szwedzkiego.

%package lang-syr
Summary:	Syriac language data for Tesseract
Summary(pl.UTF-8):	Dane języka syryjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-syr
This package contains the data files required to recognize Syriac
language.

%description lang-syr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
syryjskiego.

%package lang-ta
Summary:	Tamil language data for Tesseract
Summary(pl.UTF-8):	Dane języka tamilskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ta
This package contains the data files required to recognize Tamil
language.

%description lang-ta -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tamilskiego.

%package lang-tt
Summary:	Tatar language data for Tesseract
Summary(pl.UTF-8):	Dane języka tatarskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-tt
This package contains the data files required to recognize Tatar
language.

%description lang-tt -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tatarskiego.

%package lang-te
Summary:	Telugu language data for Tesseract
Summary(pl.UTF-8):	Dane języka telugu dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-te
This package contains the data files required to recognize Telugu
language.

%description lang-te -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
telugu.

%package lang-tg
Summary:	Tajik language data for Tesseract
Summary(pl.UTF-8):	Dane języka tadżyckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-tg
This package contains the data files required to recognize Tajik
language.

%description lang-tg -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tadżyckiego.

%package lang-tl
Summary:	Tagalog language data for Tesseract
Summary(pl.UTF-8):	Dane języka tagalskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-tl

%description lang-tl
This package contains the data files required to recognize Tagalog
language.

%description lang-tl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tagalskiego.

%package lang-th
Summary:	Thai language data for Tesseract
Summary(pl.UTF-8):	Dane języka tajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-th

%description lang-th
This package contains the data files required to recognize Thai
language.

%description lang-th -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tajskiego.

%package lang-ti
Summary:	Tigrinya language data for Tesseract
Summary(pl.UTF-8):	Dane języka tigrinia dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ti
This package contains the data files required to recognize Tigrinya
language.

%description lang-ti -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tigrinia.

%package lang-to
Summary:	Tongan language data for Tesseract
Summary(pl.UTF-8):	Dane języka tonga (z Wysp Tonga) dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-to
This package contains the data files required to recognize Tongan
language.

%description lang-to -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tonga (z wysp Tonga).

%package lang-tr
Summary:	Turkish language data for Tesseract
Summary(pl.UTF-8):	Dane języka tureckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-tr

%description lang-tr
This package contains the data files required to recognize Turkish
language.

%description lang-tr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
tureckiego.

%package lang-ug
Summary:	Uighur language data for Tesseract
Summary(pl.UTF-8):	Dane języka ujgurskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ug
This package contains the data files required to recognize Uighur
language.

%description lang-ug -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
ujgurskiego.

%package lang-uk
Summary:	Ukrainian language data for Tesseract
Summary(pl.UTF-8):	Dane języka ukraińskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-uk

%description lang-uk
This package contains the data files required to recognize Ukrainian
language.

%description lang-uk -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
ukraińskiego.

%package lang-ur
Summary:	Urdu language data for Tesseract
Summary(pl.UTF-8):	Dane języka urdu dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-ur
This package contains the data files required to recognize Urdu
language.

%description lang-ur -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
urdu.

%package lang-uz
Summary:	Uzbek language data for Tesseract
Summary(pl.UTF-8):	Dane języka uzbeckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-uz
This package contains the data files required to recognize Uzbek
language.

%description lang-uz -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
uzbeckiego.

%package lang-vi
Summary:	Vietnamese language data for Tesseract
Summary(pl.UTF-8):	Dane języka wietnamskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}
Obsoletes:	tesseract-lang-vi

%description lang-vi
This package contains the data files required to recognize Vietnamese
language.

%description lang-vi -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
wietnamskiego.

%package lang-yi
Summary:	Yiddish language data for Tesseract
Summary(pl.UTF-8):	Dane języka jidysz dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-yi
This package contains the data files required to recognize Yiddish
language.

%description lang-yi -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
jidysz.

%package lang-yo
Summary:	Yoruba language data for Tesseract
Summary(pl.UTF-8):	Dane języka joruba dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description lang-yo
This package contains the data files required to recognize Yoruba
language.

%description lang-yo -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania języka
joruba.

%package script-Arab
Summary:	Arabic script data for Tesseract
Summary(pl.UTF-8):	Dane pisma arabskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Arab
This package contains the data files required to recognize Arabic
script.

%description script-Arab -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
arabskiego.

%package script-Armn
Summary:	Armenian script data for Tesseract
Summary(pl.UTF-8):	Dane pisma ormiańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Armn
This package contains the data files required to recognize Armenian
script.

%description script-Armn -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
ormiańskiego.

%package script-Beng
Summary:	Bengali script data for Tesseract
Summary(pl.UTF-8):	Dane pisma bengalskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Beng
This package contains the data files required to recognize Bengali
script.

%description script-Beng -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
bengalskiego.

%package script-Cans
Summary:	Canadian Aboriginal script data for Tesseract
Summary(pl.UTF-8):	Dane pisma kanadyjskich autochtonów dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Cans
This package contains the data files required to recognize Canadian
Aboriginal script.

%description script-Cans -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
kanadyjskich autochtonów.

%package script-Cher
Summary:	Cherokee script data for Tesseract
Summary(pl.UTF-8):	Dane pisma czerokeskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Cher
This package contains the data files required to recognize Cherokee
script.

%description script-Cher -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
czerokeskiego.

%package script-Cyrl
Summary:	Cyrillic script data for Tesseract
Summary(pl.UTF-8):	Dane cyrylicy dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Cyrl
This package contains the data files required to recognize Cyrillic
script.

%description script-Cyrl -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania cyrylicy.

%package script-Deva
Summary:	Devanagari script data for Tesseract
Summary(pl.UTF-8):	Dane pisma dewanagari dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Deva
This package contains the data files required to recognize Devanagari
script.

%description script-Deva -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
dewanagari.

%package script-Ethi
Summary:	Ethiopic script data for Tesseract
Summary(pl.UTF-8):	Dane pisma etiopskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Ethi
This package contains the data files required to recognize Ethiopic
script.

%description script-Ethi -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
etiopskiego.

%package script-Latf
Summary:	Latin Fraktur script data for Tesseract
Summary(pl.UTF-8):	Dane fraktury łacińskiej dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Latf
This package contains the data files required to recognize Latin
Fraktur script.

%description script-Latf -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania fraktury
łacińskiej.

%package script-Geor
Summary:	Georgian script data for Tesseract
Summary(pl.UTF-8):	Dane pisma gruzińskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Geor
This package contains the data files required to recognize Georgian
script.

%description script-Geor -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
gruzińskiego.

%package script-Grek
Summary:	Greek script data for Tesseract
Summary(pl.UTF-8):	Dane pisma greckiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Grek
This package contains the data files required to recognize Greek
script.

%description script-Grek -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
greckiego.

%package script-Gujr
Summary:	Gujarati script data for Tesseract
Summary(pl.UTF-8):	Dane pisma gudźarati dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Gujr
This package contains the data files required to recognize Gujarati
script.

%description script-Gujr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
gudźarati.

%package script-Guru
Summary:	Gurmukhi script data for Tesseract
Summary(pl.UTF-8):	Dane pisma gurmukhi dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Guru
This package contains the data files required to recognize Gurmukhi
script.

%description script-Guru -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
gurmukhi.

%package script-Hans
Summary:	Han (simplified variant) script data for Tesseract
Summary(pl.UTF-8):	Dane pisma chińskiego uproszczonego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Hans
This package contains the data files required to recognize Han script
in simplified variant.

%description script-Hans -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
chińskiego uproszczonego.

%package script-Hant
Summary:	Han (tranditional variant) script data for Tesseract
Summary(pl.UTF-8):	Dane pisma chińskiego tradycyjnego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Hant
This package contains the data files required to recognize Han script
in tranditional variant.

%description script-Hant -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
chińskiego tradycyjnego.

%package script-Hang
Summary:	Hangul script data for Tesseract
Summary(pl.UTF-8):	Dane pisma hangyl dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Hang
This package contains the data files required to recognize Hangul
script.

%description script-Hang -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
hangyl.

%package script-Hebr
Summary:	Hebrew script data for Tesseract
Summary(pl.UTF-8):	Dane pisma hebrajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Hebr
This package contains the data files required to recognize Hebrew
script.

%description script-Hebr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
hebrajskiego.

%package script-Hrkt
Summary:	Japanese (Hiragana and Katakana) script data for Tesseract
Summary(pl.UTF-8):	Dane pisma japońskiego (hiragana i katakana) dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Hrkt
This package contains the data files required to recognize Japanese
(Hiragana and Katakana) script.

%description script-Hrkt -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
japońskiego (hiragana i katakana).

%package script-Knda
Summary:	Kannada script data for Tesseract
Summary(pl.UTF-8):	Dane pisma kannada dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Knda
This package contains the data files required to recognize Kannada
script.

%description script-Knda -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
kannada.

%package script-Khmr
Summary:	Khmer script data for Tesseract
Summary(pl.UTF-8):	Dane pisma khmerskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Khmr
This package contains the data files required to recognize Khmer
script.

%description script-Khmr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
khmerskiego.

%package script-Laoo
Summary:	Lao script data for Tesseract
Summary(pl.UTF-8):	Dane pisma laotańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Laoo
This package contains the data files required to recognize Lao script.

%description script-Laoo -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
laotańskiego.

%package script-Latn
Summary:	Latin script data for Tesseract
Summary(pl.UTF-8):	Dane pisma łacińskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Latn
This package contains the data files required to recognize Latin
script.

%description script-Latn -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
łacińskiego.

%package script-Mlym
Summary:	Malayalam script data for Tesseract
Summary(pl.UTF-8):	Dane pisma malajalam dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Mlym
This package contains the data files required to recognize Malayalam
script.

%description script-Mlym -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
malajalam.

%package script-Mymr
Summary:	Myanmar script data for Tesseract
Summary(pl.UTF-8):	Dane pisma birmańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Mymr
This package contains the data files required to recognize Myanmar
script.

%description script-Mymr -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
birmańskiego.

%package script-Orya
Summary:	Oriya script data for Tesseract
Summary(pl.UTF-8):	Dane pisma orija dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Orya
This package contains the data files required to recognize Oriya
script.

%description script-Orya -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
orija.

%package script-Sinh
Summary:	Sinhala script data for Tesseract
Summary(pl.UTF-8):	Dane pisma syngaleskiego (sinhala) dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Sinh
This package contains the data files required to recognize Sinhala
script.

%description script-Sinh -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
syngaleskiego (sinhala).

%package script-Syrc
Summary:	Syriac script data for Tesseract
Summary(pl.UTF-8):	Dane pisma syryjskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Syrc
This package contains the data files required to recognize Syriac
script.

%description script-Syrc -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
syryjskiego.

%package script-Taml
Summary:	Tamil script data for Tesseract
Summary(pl.UTF-8):	Dane pisma tamilskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Taml
This package contains the data files required to recognize Tamil
script.

%description script-Taml -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
tamilskiego.

%package script-Telu
Summary:	Telugu script data for Tesseract
Summary(pl.UTF-8):	Dane pisma telugu dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Telu
This package contains the data files required to recognize Telugu
script.

%description script-Telu -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
telugu.

%package script-Thaa
Summary:	Thaana script data for Tesseract
Summary(pl.UTF-8):	Dane pisma thaana dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Thaa
This package contains the data files required to recognize Thaana
script.

%description script-Thaa -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
thaana.

%package script-Thai
Summary:	Thai script data for Tesseract
Summary(pl.UTF-8):	Dane pisma tajskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Thai
This package contains the data files required to recognize Thai
script.

%description script-Thai -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
tajskiego.

%package script-Tibt
Summary:	Tibetan script data for Tesseract
Summary(pl.UTF-8):	Dane pisma tybetańskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Tibt
This package contains the data files required to recognize Tibetan
script.

%description script-Tibt -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
tybetańskiego.

%package script-Vietnamese
Summary:	Vietnamese script data for Tesseract
Summary(pl.UTF-8):	Dane pisma wietnamskiego dla Tesseracta
Group:		Applications/Graphics
Requires:	tesseract >= %{tesseract_ver}
Provides:	tesseract-data = %{version}

%description script-Vietnamese
This package contains the data files required to recognize Vietnamese
script.

%description script-Vietnamese -l pl.UTF-8
Ten pakiet zawiera pliki danych potrzebne do rozpoznawania pisma
wietnamskiego.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

# extract directly to buildroot to avoid copying 1+GB of data
%{__tar} xf %{SOURCE0} -C $RPM_BUILD_ROOT%{_datadir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/tessdata-%{version} $RPM_BUILD_ROOT%{_datadir}/tessdata

%{__rm} $RPM_BUILD_ROOT%{_datadir}/tessdata/{.gitmodules,LICENSE}

# packaged in tesseract
%{__rm} $RPM_BUILD_ROOT%{_datadir}/tessdata/{configs,pdf.ttf}

# FIXME: package in some common subpackage?
#install -d $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#%{__mv} $RPM_BUILD_ROOT%{_datadir}/tessdata/README.md $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -p %{SOURCE10} $RPM_BUILD_ROOT%{_datadir}/tessdata

%clean
rm -rf $RPM_BUILD_ROOT

%files equ
%defattr(644,root,root,755)
%{_datadir}/tessdata/equ.traineddata

%files osd
%defattr(644,root,root,755)
%{_datadir}/tessdata/osd.traineddata

%files lang-af
%defattr(644,root,root,755)
%{_datadir}/tessdata/afr.traineddata

%files lang-am
%defattr(644,root,root,755)
%{_datadir}/tessdata/amh.traineddata

%files lang-ar
%defattr(644,root,root,755)
%{_datadir}/tessdata/ara.traineddata

%files lang-as
%defattr(644,root,root,755)
%{_datadir}/tessdata/asm.traineddata

%files lang-az
%defattr(644,root,root,755)
%{_datadir}/tessdata/aze.traineddata
%{_datadir}/tessdata/aze_cyrl.traineddata

%files lang-be
%defattr(644,root,root,755)
%{_datadir}/tessdata/bel.traineddata

%files lang-bn
%defattr(644,root,root,755)
%{_datadir}/tessdata/ben.traineddata

%files lang-bo
%defattr(644,root,root,755)
%{_datadir}/tessdata/bod.traineddata

%files lang-bs
%defattr(644,root,root,755)
%{_datadir}/tessdata/bos.traineddata

%files lang-br
%defattr(644,root,root,755)
%{_datadir}/tessdata/bre.traineddata

%files lang-bg
%defattr(644,root,root,755)
%{_datadir}/tessdata/bul.traineddata

%files lang-ca
%defattr(644,root,root,755)
%{_datadir}/tessdata/cat.traineddata

%files lang-ceb
%defattr(644,root,root,755)
%{_datadir}/tessdata/ceb.traineddata

%files lang-cs
%defattr(644,root,root,755)
%{_datadir}/tessdata/ces.traineddata

%files lang-zh_CN
%defattr(644,root,root,755)
%{_datadir}/tessdata/chi_sim.traineddata
%{_datadir}/tessdata/chi_sim_vert.traineddata

%files lang-zh_TW
%defattr(644,root,root,755)
%{_datadir}/tessdata/chi_tra.traineddata
%{_datadir}/tessdata/chi_tra_vert.traineddata

%files lang-chr
%defattr(644,root,root,755)
%{_datadir}/tessdata/chr.traineddata

%files lang-co
%defattr(644,root,root,755)
%{_datadir}/tessdata/cos.traineddata

%files lang-cy
%defattr(644,root,root,755)
%{_datadir}/tessdata/cym.traineddata

%files lang-da
%defattr(644,root,root,755)
%{_datadir}/tessdata/dan.traineddata
%{_datadir}/tessdata/dan_frak.traineddata

%files lang-de
%defattr(644,root,root,755)
%{_datadir}/tessdata/deu.traineddata
%{_datadir}/tessdata/deu_frak.traineddata

%files lang-dv
%defattr(644,root,root,755)
%{_datadir}/tessdata/div.traineddata

%files lang-dz
%defattr(644,root,root,755)
%{_datadir}/tessdata/dzo.traineddata

%files lang-el
%defattr(644,root,root,755)
%{_datadir}/tessdata/ell.traineddata

%files lang-en
%defattr(644,root,root,755)
%{_datadir}/tessdata/eng.traineddata

%files lang-enm
%defattr(644,root,root,755)
%{_datadir}/tessdata/enm.traineddata

%files lang-eo
%defattr(644,root,root,755)
%{_datadir}/tessdata/epo.traineddata

%files lang-et
%defattr(644,root,root,755)
%{_datadir}/tessdata/est.traineddata

%files lang-eu
%defattr(644,root,root,755)
%{_datadir}/tessdata/eus.traineddata

%files lang-fo
%defattr(644,root,root,755)
%{_datadir}/tessdata/fao.traineddata

%files lang-fa
%defattr(644,root,root,755)
%{_datadir}/tessdata/fas.traineddata

%files lang-fil
%defattr(644,root,root,755)
%{_datadir}/tessdata/fil.traineddata

%files lang-fi
%defattr(644,root,root,755)
%{_datadir}/tessdata/fin.traineddata

%files lang-fr
%defattr(644,root,root,755)
%{_datadir}/tessdata/fra.traineddata

%files lang-frk
%defattr(644,root,root,755)
%{_datadir}/tessdata/frk.traineddata

%files lang-frm
%defattr(644,root,root,755)
%{_datadir}/tessdata/frm.traineddata

%files lang-fy
%defattr(644,root,root,755)
%{_datadir}/tessdata/fry.traineddata

%files lang-gd
%defattr(644,root,root,755)
%{_datadir}/tessdata/gla.traineddata

%files lang-ga
%defattr(644,root,root,755)
%{_datadir}/tessdata/gle.traineddata

%files lang-gl
%defattr(644,root,root,755)
%{_datadir}/tessdata/glg.traineddata

%files lang-grc
%defattr(644,root,root,755)
%{_datadir}/tessdata/grc.traineddata

%files lang-gu
%defattr(644,root,root,755)
%{_datadir}/tessdata/guj.traineddata

%files lang-ht
%defattr(644,root,root,755)
%{_datadir}/tessdata/hat.traineddata

%files lang-he
%defattr(644,root,root,755)
%{_datadir}/tessdata/heb.traineddata

%files lang-hi
%defattr(644,root,root,755)
%{_datadir}/tessdata/hin.traineddata

%files lang-hr
%defattr(644,root,root,755)
%{_datadir}/tessdata/hrv.traineddata

%files lang-hu
%defattr(644,root,root,755)
%{_datadir}/tessdata/hun.traineddata

%files lang-hy
%defattr(644,root,root,755)
%{_datadir}/tessdata/hye.traineddata

%files lang-iu
%defattr(644,root,root,755)
%{_datadir}/tessdata/iku.traineddata

%files lang-id
%defattr(644,root,root,755)
%{_datadir}/tessdata/ind.traineddata

%files lang-is
%defattr(644,root,root,755)
%{_datadir}/tessdata/isl.traineddata

%files lang-it
%defattr(644,root,root,755)
%{_datadir}/tessdata/ita.traineddata
%{_datadir}/tessdata/ita_old.traineddata

%files lang-jv
%defattr(644,root,root,755)
%{_datadir}/tessdata/jav.traineddata

%files lang-ja
%defattr(644,root,root,755)
%{_datadir}/tessdata/jpn.traineddata
%{_datadir}/tessdata/jpn_vert.traineddata

%files lang-kn
%defattr(644,root,root,755)
%{_datadir}/tessdata/kan.traineddata

%files lang-ka
%defattr(644,root,root,755)
%{_datadir}/tessdata/kat.traineddata
%{_datadir}/tessdata/kat_old.traineddata

%files lang-kk
%defattr(644,root,root,755)
%{_datadir}/tessdata/kaz.traineddata

%files lang-km
%defattr(644,root,root,755)
%{_datadir}/tessdata/khm.traineddata

%files lang-ky
%defattr(644,root,root,755)
%{_datadir}/tessdata/kir.traineddata

%files lang-kmr
%defattr(644,root,root,755)
%{_datadir}/tessdata/kmr.traineddata

%files lang-ko
%defattr(644,root,root,755)
%{_datadir}/tessdata/kor.traineddata
%{_datadir}/tessdata/kor_vert.traineddata

%files lang-ku
%defattr(644,root,root,755)
%{_datadir}/tessdata/kur.traineddata

%files lang-lo
%defattr(644,root,root,755)
%{_datadir}/tessdata/lao.traineddata

%files lang-la
%defattr(644,root,root,755)
%{_datadir}/tessdata/lat.traineddata

%files lang-lv
%defattr(644,root,root,755)
%{_datadir}/tessdata/lav.traineddata

%files lang-lt
%defattr(644,root,root,755)
%{_datadir}/tessdata/lit.traineddata

%files lang-lb
%defattr(644,root,root,755)
%{_datadir}/tessdata/ltz.traineddata

%files lang-ml
%defattr(644,root,root,755)
%{_datadir}/tessdata/mal.traineddata

%files lang-mr
%defattr(644,root,root,755)
%{_datadir}/tessdata/mar.traineddata

%files lang-mk
%defattr(644,root,root,755)
%{_datadir}/tessdata/mkd.traineddata

%files lang-mt
%defattr(644,root,root,755)
%{_datadir}/tessdata/mlt.traineddata

%files lang-mn
%defattr(644,root,root,755)
%{_datadir}/tessdata/mon.traineddata

%files lang-mi
%defattr(644,root,root,755)
%{_datadir}/tessdata/mri.traineddata

%files lang-ms
%defattr(644,root,root,755)
%{_datadir}/tessdata/msa.traineddata

%files lang-my
%defattr(644,root,root,755)
%{_datadir}/tessdata/mya.traineddata

%files lang-ne
%defattr(644,root,root,755)
%{_datadir}/tessdata/nep.traineddata

%files lang-nl
%defattr(644,root,root,755)
%{_datadir}/tessdata/nld.traineddata

%files lang-nb
%defattr(644,root,root,755)
%{_datadir}/tessdata/nor.traineddata

%files lang-oc
%defattr(644,root,root,755)
%{_datadir}/tessdata/oci.traineddata

%files lang-or
%defattr(644,root,root,755)
%{_datadir}/tessdata/ori.traineddata

%files lang-pa
%defattr(644,root,root,755)
%{_datadir}/tessdata/pan.traineddata

%files lang-pl
%defattr(644,root,root,755)
%{_datadir}/tessdata/pol.traineddata

%files lang-pt
%defattr(644,root,root,755)
%{_datadir}/tessdata/por.traineddata

%files lang-ps
%defattr(644,root,root,755)
%{_datadir}/tessdata/pus.traineddata

%files lang-qu
%defattr(644,root,root,755)
%{_datadir}/tessdata/que.traineddata

%files lang-ro
%defattr(644,root,root,755)
%{_datadir}/tessdata/ron.traineddata

%files lang-ru
%defattr(644,root,root,755)
%{_datadir}/tessdata/rus.traineddata

%files lang-sa
%defattr(644,root,root,755)
%{_datadir}/tessdata/san.traineddata

%files lang-si
%defattr(644,root,root,755)
%{_datadir}/tessdata/sin.traineddata

%files lang-sk
%defattr(644,root,root,755)
%{_datadir}/tessdata/slk.traineddata
%{_datadir}/tessdata/slk_frak.traineddata

%files lang-sl
%defattr(644,root,root,755)
%{_datadir}/tessdata/slv.traineddata

%files lang-sd
%defattr(644,root,root,755)
%{_datadir}/tessdata/snd.traineddata

%files lang-es
%defattr(644,root,root,755)
%{_datadir}/tessdata/spa.traineddata
%{_datadir}/tessdata/spa_old.traineddata

%files lang-sq
%defattr(644,root,root,755)
%{_datadir}/tessdata/sqi.traineddata

%files lang-sr
%defattr(644,root,root,755)
%{_datadir}/tessdata/srp.traineddata
%{_datadir}/tessdata/srp_latn.traineddata

%files lang-su
%defattr(644,root,root,755)
%{_datadir}/tessdata/sun.traineddata

%files lang-sw
%defattr(644,root,root,755)
%{_datadir}/tessdata/swa.traineddata

%files lang-sv
%defattr(644,root,root,755)
%{_datadir}/tessdata/swe.traineddata

%files lang-syr
%defattr(644,root,root,755)
%{_datadir}/tessdata/syr.traineddata

%files lang-ta
%defattr(644,root,root,755)
%{_datadir}/tessdata/tam.traineddata

%files lang-tt
%defattr(644,root,root,755)
%{_datadir}/tessdata/tat.traineddata

%files lang-te
%defattr(644,root,root,755)
%{_datadir}/tessdata/tel.traineddata

%files lang-tg
%defattr(644,root,root,755)
%{_datadir}/tessdata/tgk.traineddata

%files lang-tl
%defattr(644,root,root,755)
%{_datadir}/tessdata/tgl.traineddata

%files lang-th
%defattr(644,root,root,755)
%{_datadir}/tessdata/tha.traineddata

%files lang-ti
%defattr(644,root,root,755)
%{_datadir}/tessdata/tir.traineddata

%files lang-to
%defattr(644,root,root,755)
%{_datadir}/tessdata/ton.traineddata

%files lang-tr
%defattr(644,root,root,755)
%{_datadir}/tessdata/tur.traineddata

%files lang-ug
%defattr(644,root,root,755)
%{_datadir}/tessdata/uig.traineddata

%files lang-uk
%defattr(644,root,root,755)
%{_datadir}/tessdata/ukr.traineddata

%files lang-ur
%defattr(644,root,root,755)
%{_datadir}/tessdata/urd.traineddata

%files lang-uz
%defattr(644,root,root,755)
%{_datadir}/tessdata/uzb.traineddata
%{_datadir}/tessdata/uzb_cyrl.traineddata

%files lang-vi
%defattr(644,root,root,755)
%{_datadir}/tessdata/vie.traineddata

%files lang-yi
%defattr(644,root,root,755)
%{_datadir}/tessdata/yid.traineddata

%files lang-yo
%defattr(644,root,root,755)
%{_datadir}/tessdata/yor.traineddata

%files script-Arab
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Arabic.traineddata

%files script-Armn
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Armenian.traineddata

%files script-Beng
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Bengali.traineddata

%files script-Cans
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Canadian_Aboriginal.traineddata

%files script-Cher
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Cherokee.traineddata

%files script-Cyrl
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Cyrillic.traineddata

%files script-Deva
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Devanagari.traineddata

%files script-Ethi
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Ethiopic.traineddata

%files script-Latf
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Fraktur.traineddata

%files script-Geor
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Georgian.traineddata

%files script-Grek
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Greek.traineddata

%files script-Gujr
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Gujarati.traineddata

%files script-Guru
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Gurmukhi.traineddata

%files script-Hans
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/HanS.traineddata
%{_datadir}/tessdata/script/HanS_vert.traineddata

%files script-Hant
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/HanT.traineddata
%{_datadir}/tessdata/script/HanT_vert.traineddata

%files script-Hang
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Hangul.traineddata
%{_datadir}/tessdata/script/Hangul_vert.traineddata

%files script-Hebr
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Hebrew.traineddata

%files script-Hrkt
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Japanese.traineddata
%{_datadir}/tessdata/script/Japanese_vert.traineddata

%files script-Knda
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Kannada.traineddata

%files script-Khmr
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Khmer.traineddata

%files script-Laoo
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Lao.traineddata

%files script-Latn
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Latin.traineddata

%files script-Mlym
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Malayalam.traineddata

%files script-Mymr
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Myanmar.traineddata

%files script-Orya
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Oriya.traineddata

%files script-Sinh
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Sinhala.traineddata

%files script-Syrc
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Syriac.traineddata

%files script-Taml
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Tamil.traineddata

%files script-Telu
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Telugu.traineddata

%files script-Thaa
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Thaana.traineddata

%files script-Thai
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Thai.traineddata

%files script-Tibt
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Tibetan.traineddata

%files script-Vietnamese
%defattr(644,root,root,755)
%{_datadir}/tessdata/script/Vietnamese.traineddata

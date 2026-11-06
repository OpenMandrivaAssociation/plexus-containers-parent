Name:		plexus-containers-parent
Version:	2.2.0
Release:	1
Summary:	Parent POM for Plexus Containers
Group:		Development/Java
License:	ASL 2.0
URL:		https://github.com/codehaus-plexus/plexus-containers
Source0:	https://repo1.maven.org/maven2/org/codehaus/plexus/plexus-containers/%{version}/plexus-containers-%{version}.pom
Source1:	https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:	noarch
BuildRequires:	python
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildRequires:	plexus-pom
BuildSystem:	maven
BuildOption:	-N validate

%description
Parent POM for Plexus Containers. plexus-component-annotations inherits
its coordinates from this POM. The annotation and metadata jars stay in
their own packages.

%prep
cp -p %{SOURCE0} pom.xml
cp -p %{SOURCE1} LICENSE
# Modules would publish jars that plexus-containers already ships.
python - <<'PY'
import re
from pathlib import Path
path = Path("pom.xml")
text = path.read_text()
text = re.sub(r"\n  <modules>.*?</modules>", "", text, count=1, flags=re.S)
path.write_text(text)
PY

%files -f .mfiles
%doc LICENSE

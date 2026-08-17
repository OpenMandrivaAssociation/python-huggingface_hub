Name:		python-huggingface_hub
Version:	1.27.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/h/huggingface_hub/huggingface_hub-%{version}.tar.gz
Summary:	Client library for the Hugging Face Hub
URL:		https://github.com/huggingface/huggingface_hub
License:	Apache-2.0
Group:		Development/Python
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
# huggingface-cli used to be a standalone project
Provides:	huggingface-cli = %{version}
Suggests:	git-lfs

%description
Client library to download and publish models, datasets and other
repositories on the Hugging Face Hub. Ships the hf / huggingface-cli
command-line tools.

%package -n huggingface
Summary:	Hugging Face CLI and Python ML stack
Group:		Development/Python
Requires:	python-huggingface_hub = %{EVRD}
Requires:	python-tokenizers
Requires:	python-safetensors
Requires:	python-transformers
Requires:	python-accelerate
Requires:	python-peft
Requires:	python-diffusers

%description -n huggingface
Meta-package pulling in huggingface-cli and the commonly used
Hugging Face Python libraries (transformers, tokenizers,
safetensors, accelerate, peft and diffusers).

%files
%doc README.md
%license LICENSE
%{_bindir}/hf
%{_bindir}/huggingface-cli
%{_bindir}/tiny-agents
%{py_sitedir}/huggingface_hub
%{py_sitedir}/huggingface_hub-*.*-info

%files -n huggingface

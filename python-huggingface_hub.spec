Name:		python-huggingface_hub
Version:	2.1.1
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
repositories on the Hugging Face Hub. Ships the hf command-line tool.

%package -n huggingface
Summary:	Hugging Face CLI and Python ML stack
Group:		Development/Python
Requires:	python-huggingface_hub = %{EVRD}
# Weak deps so extra-tests can install this metapackage before
# the rest of the stack is published.
Recommends:	python-tokenizers
Recommends:	python-safetensors
Recommends:	python-transformers
Recommends:	python-accelerate
Recommends:	python-peft
Recommends:	python-diffusers

%description -n huggingface
Meta-package pulling in the hf command-line tool and the commonly used
Hugging Face Python libraries (transformers, tokenizers,
safetensors, accelerate, peft and diffusers).

%files
%doc README.md
%license LICENSE
%{_bindir}/hf
%{_bindir}/tiny-agents
%{py_sitedir}/huggingface_hub
%{py_sitedir}/huggingface_hub-*.*-info

%files -n huggingface

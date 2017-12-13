#in progress!
#TODO everything lol 

IPYNB_FILES=$(wildcard *.ipynb)

.PHONY : env
env: environment.yml
	conda env create -f environment.yml



.PHONY: all
all: $(IPYNB_FILES)
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb1.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb2.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_lasso.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute main.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p3.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p4.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute demographics-p5.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute main.ipynb

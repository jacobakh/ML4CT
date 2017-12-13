#in progress!
#TODO everything lol 

IPYNB_FILES=$(wildcard *.ipynb)

.PHONY : env
env: environment.yml
	conda env create -f environment.yml



.PHONY: run
all: $(IPYNB_FILES)
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb1.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb2.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_lasso.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_random_forest.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_neural_nets.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute main.ipynb

.PHONY: test
	python tests.py
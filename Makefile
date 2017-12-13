

IPYNB_FILES=$(wildcard *.ipynb)

.PHONY : env #works on my machine
env: environment.yml
	conda env create -f environment.yml	

.PHONY: run 
run: $(IPYNB_FILES) #need to test on someone else's machine
	@echo Running the notebooks now! This is going to take some time... 
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb1.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb2.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_nb3.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_lasso.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_random_forest.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute counter_terrorism_neural_nets.ipynb
	jupyter nbconvert --ExecutePreprocessor.timeout=-1 --inplace --execute main.ipynb

.PHONY: test
test: #runs as expected
	python tests.py
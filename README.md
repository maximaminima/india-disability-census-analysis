# india-disability-census-analysis

The dataset was procured from:
http://www.censusindia.gov.in/2011census/Disability_Data/DISAB04-0000.xlsx
http://www.censusindia.gov.in/2011census/PCA/PCA_Highlights/pca_highlights_file/karnataka/PCA_Data%20Highlights_india_State.pdf

# Pre-requisites

1. Matplotlib
2. Pandas
3. Numpy
4. brewer2mpl
5. pylab

# Notes

1. Analysis and code to evolve as it progresses.
2. Cleanup the graph viz code to produce even better looking charts

# Inference

1. This graph tells us the states with the maximum number of disabled population for now. UP has the largest disabled population numbers, followed by Maharashtra.
Karnataka stands at 8th.

 ![Alt text](dtot.png?raw=true "Total disabled population in India")

2. Taking into account the states in large sizes, this is the sorted order for states having largest disabled population percentages taking into account the total population of the state. 

	1. Maharashtra 
	2. Andhra 
	3. Odisha 
	4. Madhya pradesh 
	5. Bihar 
	6. Karnataka 
	7. Rajasthan 
	8. UP 
	9. West Bengal 
	10. Gujarath 
	11. Tamilnadu

3. Hearing impaired population in India for each state as per 2011 census

 ![Alt text](hearing_tot.png?raw=true "Total hearing impaired population in India")

4. Hearing impaired non-working population in India for each state as per 2011 census

 ![Alt text](hearing_tot_nonworkers.png?raw=true "Total hearing impaired non-workers in India")

5. Run python hdcensus_max_nonworkers.py "state name"
	eg: python hdcensus_max_nonworkers.py kerala

	$ python hdcensus_max_nonworkers.py karnataka
	[('Mental Illness', 16611), ('In Speech', 55005), ('Mental Retardation', 74510), ('Multiple disability', 81563), ('In Hearing', 129400), ('Any Other', 135754), ('In Seeing', 160419), ('In Movement', 167041)]
	
	$ python hdcensus_max_nonworkers.py tamil nadu
	[('Mental Illness', 28484), ('In Speech', 47850), ('Multiple disability', 72662), ('In Seeing', 78245), ('Mental Retardation', 88658), ('In Hearing', 120383), ('Any Other', 134275), ('In Movement', 167374)]

	$ python hdcensus_max_nonworkers.py kerala
	[('In Speech', 28553), ('Mental Illness', 57486), ('Mental Retardation', 61161), ('Any Other', 67029), ('In Hearing', 74794), ('In Seeing', 84046), ('Multiple disability', 86313), ('In Movement', 122767)]	

    python hdcensus_max_nonworkers.py andhra pradesh
	[('Mental Illness', 33858), ('Mental Retardation', 105626), ('In Speech', 114212), ('Multiple disability', 153779), ('In Hearing', 182100), ('Any Other', 227773), ('In Seeing', 238898), ('In Movement', 335174)]

	Only southern states for now mainly Karnataka, Kerala and Tamilnadu, Andhra. Notice that bulk of the non-workers fall into movement disabled category. Another point to notice is that Andhra and Karnataka have maximum number of hearing impaired non-workers in south. With Andhra's division in recent census to Telengana and Andhra, it is possible that Karnataka might have taken lead in hearing impaired numbers, that can be verified when new census data is available.


6. More analysis to be added

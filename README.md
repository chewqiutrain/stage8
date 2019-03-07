# COTA Hackday 1Q19 
An attempt at automating the calculation of AJCC pathological prognostic stage

### Members:
1. Brooke Gruman
1. Priya Venkatesan
1. Youssef Zarrouk
1. Ashwin Lakshmanan
1. Chew Lee

## Lessons Learnt
1. The staging table in the AJCC book seems deceptively simple in its logic. The E-Book version obtained via their API expands to about 10,000 rows. i.e. 10,000 ways to stage based on inputs. 
1. In order to use the E-Book version of the table, whether T,N,M were obtained clinically or pathologically needs to be determined from the get go. NB: This does not necessarily mean that the calculated stage will be different. 
	1. For any future staging calculator, there should be an extensive suite of test cases, which need to be broken down into clinical vs pathological. 
1. COTA's T,N,M values need to be cleaned and map if we intend to use these lookup tables.

## Caveats
1. The 8th edition of AJCC staging tables can only be used for diagnosis occurring after a certain date; this hack does nothing regarding dates.
1. We did not tackle the problem of 'reduction', i.e. choosing which input values to use for staging from a given progression group / track. 

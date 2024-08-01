Shazam Research Dataset - Offsets (SRD-O) 

Shazam Entertainment, Ltd., 2016 Contact: <research@shazam.com>  

Citation 

**Citation for the dataset**: 

Shazam Entertainment, Ltd. (2016). Shazam Research Dataset - Offsets (SRD-O). Stanford Digital Repository. Available at:[ http://purl.stanford.edu/fj396zz8014](http://purl.stanford.edu/fj396zz8014) 

**If using the dataset, please also cite the following paper:** 

Blair  Kaneshiro,  Feng Ruan, Casey W. Baker, and Jonathan Berger (2017). Characterizing Listener Engagement with Popular Songs Using Large-Scale Music Discovery Data. Frontiers in Psychology 8:146. doi:10.3389/fpsyg.2017.00416 

License 

This dataset is licensed under a [Creative Commons Attribution-Noncommercial-No Derivative Works 3.0 Unported License](https://creativecommons.org/licenses/by-nc-nd/3.0/) **(CC) BY-NC-ND**. 

Abstract 

This dataset contains Shazam query timings (‘offsets’) and query dates corresponding to 20 hit songs  from  the  Billboard  Year  End  Hot  100  2015  chart.  Queries were aggregated from 1 January 2014 to 31 May 2016, inclusive. Number of queries per song range from 3,020,785 to 19,974,795, with a total of 188,271,243 queries across the 20 songs. Data are stored in .csv files (one file per song) ranging in size from 62.9MB to 416.1MB. The total size of the dataset is around 4GB. 

**Keywords**: Music discovery, Shazam, music information retrieval, multimedia search, social media, popular music, Center for Computer Research in Music and Acoustics 

Dataset files 

- **README.pdf** (this document): Informational document describing the dataset. 
- **song01.csv** through **song21.csv**: Data files for individual songs. Each .csv data file contains two columns labeled “Offset” and “Date” in the header row. The “Offset” column gives the timestamp of the query (time from the start of the song that the Shazam query was  performed)  in  seconds.  The  “Date”  column  gives  the  date  of  the  query (YYYY-MM-DD format) in GMT time.  

Data aggregation and cleaning 

Worldwide  queries  were  aggregated  from  1  January  2014  to  31 May 2016, inclusive. The present dataset has been cleaned of incomplete queries (missing date or offset), queries with offsets  less  than  or  equal  to  zero,  and  queries  with  offsets  exceeding  the  length  of  the corresponding  audio  track.  Over  95%  of  queries  for  each  song  are  still  usable  after  data cleaning (see Kaneshiro et al. (2017), Table 1 for details). 

Song list 

(See table on next page.) Numbers in .csv filenames reflect 2015 Billboard Year End Hot 100 chart positions (<http://www.billboard.com/charts/year-end/2015/hot-100-songs>). The dataset includes queries from Songs 1-21, excluding Song 15. Shazam track result webpages can be reached by appending a song’s Shazam trackid to <http://www.shazam.com/track/>. Digital versions of the tracks can be accessed on Amazon by searching for the song’s ASIN. Additional song information and metadata can be found in Kaneshiro et al. (2017), Table 1 and Table S1. 



|**Filename** |**Song/Artist** |**Shazam trackid** |**Amazon ASIN** |**# queries** |
| - | - | :- | :- | - |
|**song01.csv** |“Uptown Funk!” *Mark Ronson Feat. Bruno Mars* |160157606 |B00S226A48 |13,855,245 |
|**song02.csv** |“Thinking Out Loud” *Ed Sheeran* |123453088 |B00JLJ6VSQ |17,142,656 |
|**song03.csv** |“See You Again” *Wiz Khalifa Feat. Charlie Puth* |235243031 |B00TJ69DHM |12,522,399 |
|**song04.csv** |“Trap Queen” *Fetty Wap* |119440654 |B00QSDA4IG |6,072,939 |
|**song05.csv** |“Sugar” *Maroon 5* |144086612 |B00XDI1GEU |5,811,731 |
|**song06.csv** |“Shut Up and Dance” *Walk the Moon* |150773872 |B00P6Y1OJG |5,034,637 |
|**song07.csv** |“Blank Space” *Taylor Swift* |157666207 |B00OXE38D0 |6,764,128 |
|**song08.csv** |“Watch Me” *Silento* |229572648 |B00X5MVZ6I |4,463,863 |
|**song09.csv** |“Earned It (Fifty Shades of Grey)” *The Weeknd* |221708306 |B00S17FWPW |7,514,440 |
|**song10.csv** |“The Hills” *The Weeknd* |267041500 |B014DIAKRM |8,657,473 |
|**song11.csv** |“Cheerleader (Felix Jaehn Remix)” *OMI* |119205187 |B01HPWYZTC |17,933,224 |
|**song12.csv** |“Can’t Feel My Face” *The Weeknd* |269065410 |B014DIAVS0 |8,675,375 |
|**song13.csv** |“Love Me Like You Do” *Ellie Goulding* |221827125 |B00S17FZ7C |9,925,090 |
|**song14.csv** |“Take Me to Church” *Hozier* |92719600 |B00M01JCAQ |15,854,482 |
|**song16.csv** |“Lean On” *Major Lazer & DJ Snake Feat. M0* |234782921 |B00YIAXFG4 |19,974,795 |
|**song17.csv** |“Want to Want Me” *Jason Derulo* |238644669 |B00VM6SI5K |9,885,505 |
|**song18.csv** |“Shake It Off” *Taylor Swift* |147771254 |B00OXE3GEG |3,162,707 |
|**song19.csv** |“Where Are Ü Now” *Skrillex & Diplo with Justin Bieber* |236350641 |B00U0AIECQ |7,639,899 |
|**song20.csv** |“Fight Song” *Rachel Platten* |154437676 |B0189VVN5W |4,359,870 |
|**song21.csv** |“679” *Fetty Wap Feat. Remy Boyz* |228968059 |B010DROMFI |3,020,785 |
|**Total** |188,271,243 ||||


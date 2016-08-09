#!/usr/bin/perl

# pfi.pl - Popular First Initials
# Ranks first initials in order of popularity, per the 1990 US Census
#
# Usage:
# cat dist.female.first.txt dist.female.first.txt| pfi.pl |sort -rn -k2

# Data source: http://www2.census.gov/topics/genealogy/1990surnames/
# http://www2.census.gov/topics/genealogy/1990surnames/dist.female.first
# http://www2.census.gov/topics/genealogy/1990surnames/dist.male.first
# 
# Data skews older ("Mary" is the most common first female name), do not
# have comprehensive list of more rcent first names (such as the 2000 census)

my %total; # Hash of total percentage of popularity of first initial
my @line;  # Array of current input line
my $init;  # First initial
my $key;   # for iterating through total hash
while (<>){
  chomp;
  @line=split(" ");
  $init=lc substr($line[0], 0, 1);
  $total{$init}+=$line[1];
}
foreach $key (keys %total) {
    printf ("%s %.2f\n",$key,$total{$key});
}

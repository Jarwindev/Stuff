import itertools

s1 = "abcdef"
s2 = "qprstu"

# Combine letters from s1 and s2 alternately into s3.
# Works even when s1 and s2 have different lengths.
s3_parts = []
for a, b in itertools.zip_longest(s1, s2, fillvalue=""):
	s3_parts.append(a)
	s3_parts.append(b)

s3 = "".join(s3_parts)
print(s3)
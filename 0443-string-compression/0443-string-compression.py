class Solution:
    def compress(self, chars: List[str]) -> int:
        write,count =0,1
        for read in range(1,len(chars)):
            if chars[read-1] != chars[read]:
                chars[write] = chars[read-1]
                write+=1
                if count !=1 and count <10:
                    chars[write] = str(count)
                    write+=1
                elif count !=1 and count >=10:
                    for ch in str(count):
                        chars[write] = ch
                        write+=1
                count =1
            else: 
                count +=1
        chars[write] = chars[len(chars)-1]
        write+=1
        if count !=1 and count <10:
            chars[write] = str(count)
            write+=1
        elif count !=1 and count >=10:
            for ch in str(count):
                chars[write] = ch
                write+=1
        count =1
        return write
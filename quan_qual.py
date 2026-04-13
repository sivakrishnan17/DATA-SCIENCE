
class Univariant():
    def QuanQual(data): 
        quan=[]
        qual=[]  
        for i in data.columns:
            if data[i].dtype==int or data[i].dtype==float:
                quan.append(i)
            else:
                qual.append(i)
        return qual,qual

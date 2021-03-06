from flask import send_file
from Five_W_One_H import *
from Video_Processing_Final import *
from flask import Flask, request
import csv

app = Flask(__name__)

@app.route('/get_video')
def video_processing():
    post_title          = request.args.get("title")
    post_text           = request.args.get("post_text")
    post_Complete_Text  = request.args.get("full_summary")
    csvRow = [post_title, post_text, post_Complete_Text]
    
    csvfile = "data.csv"
    with open(csvfile, "a") as fp:
         wr = csv.writer(fp, dialect='excel')
         wr.writerow(csvRow)
         
    links               = result_links(post_text,post_title,post_Complete_Text) 
    file_name           = Video_Processing(links,post_title,post_text)
    
    print("File Created::",file_name)
    return "working"

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004)
    print("App running on localhost:5004")  
    
#post_title="महिला कोच ने निक जोनस को याद दिलाया- मैं आपसे 10 साल बड़ी हूं"
#post_text="बॉलीवुड एक्ट्रेस प्रियंका चोपड़ा के पति अमरीकन गायक निक जोनस एक बार फिर दोनों की उम्र में अंतर को लेकर चर्चा में हैं। एक पॉपुलर मैगजीन ने भी जब यही सवाल पूछा तो एक्ट्रेस ने करारा जवाब देते हुए कहा कि जब पुरुष की उम्र ज्यादा हो तो कोई सवाल नहीं करता , लेकिन महिला ज्यादा उम्र की हो तो सवाल क्यों होते हैं "
#post_Complete_Text="मुंबई. बॉलीवुड एक्ट्रेस प्रियंका चोपड़ा के पति अमरीकन गायक निक जोनस एक बार फिर दोनों की उम्र में अंतर को लेकर चर्चा में हैं. उनसे एक महिला सिंगिंग कोच ने अपनी उम्र का और निक की उम्र में अंतर बताया. फिर क्या था, प्रियंका का जिक्र तो आना ही था. ये मेजदार बातचीत अमरीका के सिंगिंग रियलिटी शो 'द वायस' में सामने आई.अमरीकी रियलिटी सिंगिंग शो ' द वायस' में पहली बार सिंगिंग कोच के रूप में निक जोनस पहुंचे. उनका ये पहला एपिसोड ही था. एक कंटेस्टेंट की गायकी पर कोच बात कर रहे थे. अचानक एक महिला कोच कैली क्लार्कसन ने निक से कहा,' मैं तुमसे 10 साल बड़ी हूं. मेरी उम्र 37 साल है.' इस पर निक जोनस ने बड़ी चालाकी से जवाब दिया,' मेरी पत्नी प्रियंका भी 37 साल की हैं.' इस पर पूरे शो में हंसी के ठहाके गूंज उठे. शो के एक और कोच ब्लैक शेल्टन ने भी निक का स्वागत इसी तरह से किया था. उन्होंने निक का मजाक बनाते हुए कहा,'मैं शो के नियम जरूर पढूंगा क्योंकि ये मेरा शो है. मुझे पक्का पता नहीं है कि आप द वायस शो के कोच बनने के लिए जरूरी उम्र के हैं की नहीं, लेकिन ये अच्छे से पता है कि आपकी यहां खूब खिंचाई होने वाली है.' इस के जवाब में निक ने कहा, कम उम्र के बावजूद उनके पास 20 साल का अनुभव है. प्रियंका से भी उनके और निक की उम्र में अंतर को लेकर सवाल किए जाते रहे हैं. एक पॉपुलर मैगजीन ने भी जब यही सवाल पूछा तो एक्ट्रेस ने करारा जवाब देते हुए कहा कि जब पुरुष की उम्र ज्यादा हो तो कोई सवाल नहीं करता, लेकिन महिला ज्यादा उम्र की हो तो सवाल क्यों होते हैं."
# =============================================================================
# 
# from flask import send_file
# from Five_W_One_H import *
# from Video_Processing_Final import *
# from flask import Flask, request
# import csv
# 
# links       = result_links(post_text,post_title,post_Complete_Text) 
# file_name   = Video_Processing(links,post_title,post_text)
# 
# csvRow = [post_title, post_text, post_Complete_Text]
# csvfile = "data.csv"
# with open(csvfile, "a") as fp:
#     wr = csv.writer(fp, dialect='excel')
#     wr.writerow(csvRow)
# 
# 
# =============================================================================

#49.156.128.11:5004/get_video?title='''महिला कोच ने निक जोनस को याद दिलाया- मैं आपसे 10 साल बड़ी हूं'''&post_text='''बॉलीवुड एक्ट्रेस प्रियंका चोपड़ा के पति अमरीकन गायक निक जोनस एक बार फिर दोनों की उम्र में अंतर को लेकर चर्चा में हैं। एक पॉपुलर मैगजीन ने भी जब यही सवाल पूछा तो एक्ट्रेस ने करारा जवाब देते हुए कहा कि जब पुरुष की उम्र ज्यादा हो तो कोई सवाल नहीं करता , लेकिन महिला ज्यादा उम्र की हो तो सवाल क्यों होते हैं '''&full_summary='''मुंबई. बॉलीवुड एक्ट्रेस प्रियंका चोपड़ा के पति अमरीकन गायक निक जोनस एक बार फिर दोनों की उम्र में अंतर को लेकर चर्चा में हैं. उनसे एक महिला सिंगिंग कोच ने अपनी उम्र का और निक की उम्र में अंतर बताया. फिर क्या था, प्रियंका का जिक्र तो आना ही था. ये मेजदार बातचीत अमरीका के सिंगिंग रियलिटी शो 'द वायस' में सामने आई.अमरीकी रियलिटी सिंगिंग शो ' द वायस' में पहली बार सिंगिंग कोच के रूप में निक जोनस पहुंचे. उनका ये पहला एपिसोड ही था. एक कंटेस्टेंट की गायकी पर कोच बात कर रहे थे. अचानक एक महिला कोच कैली क्लार्कसन ने निक से कहा,' मैं तुमसे 10 साल बड़ी हूं. मेरी उम्र 37 साल है.' इस पर निक जोनस ने बड़ी चालाकी से जवाब दिया,' मेरी पत्नी प्रियंका भी 37 साल की हैं.' इस पर पूरे शो में हंसी के ठहाके गूंज उठे. शो के एक और कोच ब्लैक शेल्टन ने भी निक का स्वागत इसी तरह से किया था. उन्होंने निक का मजाक बनाते हुए कहा,'मैं शो के नियम जरूर पढूंगा क्योंकि ये मेरा शो है. मुझे पक्का पता नहीं है कि आप द वायस शो के कोच बनने के लिए जरूरी उम्र के हैं की नहीं, लेकिन ये अच्छे से पता है कि आपकी यहां खूब खिंचाई होने वाली है.' इस के जवाब में निक ने कहा, कम उम्र के बावजूद उनके पास 20 साल का अनुभव है. प्रियंका से भी उनके और निक की उम्र में अंतर को लेकर सवाल किए जाते रहे हैं. एक पॉपुलर मैगजीन ने भी जब यही सवाल पूछा तो एक्ट्रेस ने करारा जवाब देते हुए कहा कि जब पुरुष की उम्र ज्यादा हो तो कोई सवाल नहीं करता, लेकिन महिला ज्यादा उम्र की हो तो सवाल क्यों होते हैं.'''




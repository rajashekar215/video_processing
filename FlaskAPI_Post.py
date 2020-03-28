from flask import send_file,send_from_directory
from Five_W_One_H import *
from Video_Processing_Final import *
from flask import Flask, request
import csv

UPLOAD_DIRECTORY='/root/avinash/Video_Generation_Complete/VIDEO'

app = Flask(__name__)

@app.route('/get_video', methods=['POST'])
def video_processing():
    post_title          = request.json.get("title")
    post_text           = request.json.get("post_text")
    post_Complete_Text  = request.json.get("full_summary")
    post_Manual_links   = request.json.get("manual_links")
    csvRow = [post_title, post_text, post_Complete_Text]
    
    csvfile = "data.csv"
    with open(csvfile, "a") as fp:
         wr = csv.writer(fp, dialect='excel')
         wr.writerow(csvRow)
         
    links               = result_links(post_text,post_title,post_Complete_Text,post_Manual_links) 
    
    if len(post_Manual_links)==0:
        file_name           = Video_Processing(links,post_title,post_text)
    else:
        file_name           = Video_Processing(post_Manual_links,post_title,post_text)
        
    if file_name[0]:
        return send_from_directory(UPLOAD_DIRECTORY, file_name[0], as_attachment=True)
    else:
        return file_name[1]
    
    #return file_name

if __name__ == '__main__':
    app.run(threaded=False,host='49.156.128.11',port=5004)
    #print("App running on localhost:5004")  

# =============================================================================
# post_title="दिल्ली हिंसा पर ईरान के विदेश मंत्री के ट्वीट पर भारत ने जताई आपत्ति"
# post_text='''भारत ने इस मामले में मंगलवार को ईरान के राजदूत अली चेगेनी को तलब किया। बीते हफ्ते दिल्ली हिंसा का जिक्र करते हुए तुर्की के राष्ट्रपति रजब तैयब एर्दोग़ान ने दावा किया था कि भारत में एक संप्रदाय के लोगों को निशाना बनाया जा रहा है। इससे पहले मलयोशिया के पीएम महातिर मोहम्मद ने सीएए के खिलाफ दिसंबर में बयान दिया था। इन सभी पर भारत ने आपत्ति जताई '''
# post_Complete_Text='''नई दिल्ली. दिल्ली हिंसा को लेकर ईरान के विदेश मंत्री जवाद जरीफ के ट्वीट पर भारत ने कड़ी आपत्ति जताई है. भारत ने इस मामले में मंगलवार को ईरान के राजदूत अली चेगेनी को तलब किया. मीडिया रिपोर्ट के अनुसार ईरान के राजदूत को बताया गया कि यह भारत का आतंरिक मामला है और इस पर उन्हें टिप्पणी नहीं करनी चाहिए.
# नवाज शरीफ के लिए संभव नहीं है पाक आना, ब्रिटेन में होगी सर्जरी
# सोमवार को जरीफ ने ट्वीट कर कहा कि ईरान भारतीय मुस्लिमों के खिलाफ संगठित हिंसा की घटनाओं की निंदा करता है. सदियों से ईरान भारत का दोस्त रहा है. वह भारतीय अधिकारियों से आग्रह करते हैं कि वे सभी भारतीयों की सलामती सुनिश्चित करें और हिंसा को रोकने का प्रयास करें. शांतिपूर्ण संवाद और कानून का पालने करने पर ही इसका रास्ता निकलेगा.
# सूत्रों के अनुसार दिल्ली में ईरान के राजदूत अली चेगेनी को मंगलवार तलब किया गया. जाफरी द्वारा भारत के आंतरिक मामले पर टिप्पणियां को लेकर कड़ा विरोध जताया गया. बीते हफ्ते दिल्ली हिंसा का जिक्र करते हुए तुर्की के राष्ट्रपति रजब तैयब एर्दोग़ान ने दावा किया था कि भारत में एक संप्रदाय के लोगों को निशाना बनाया जा रहा है. इससे पहले मलयोशिया के पीएम महातिर मोहम्मद ने सीएए के खिलाफ दिसंबर में बयान दिया था. इन सभी पर भारत ने आपत्ति जताई.'''
# =============================================================================
# =============================================================================
# post_title="अनुच्छेद 370: सुप्रीम कोर्ट का फैसला, बड़ी बेंच के पास नहीं भेजा जाएगा केस"
# post_text='''बीते साल पांच अगस्त को केंद्र सरकार ने जम्मू कश्मीर से आर्टिकल 370 को हटा दिया था। एनजीओ पीपुल्स यूनियन ऑफ सिविल लिबर्टीज , जम्मू और कश्मीर हाई कोर्ट बार एसोसिएशन और हस्तक्षेपकर्ता ने मामले को बड़ी पीठ के पास भेजने के लिए कहा है। उन्होंने यह मांग सर्वोच्च अदालत के दो फैसले के आधार पर की है '''
# post_Complete_Text='''नई दिल्ली. उच्चतम न्यायालय सोमवार को कहा कि आर्टिकल 370 पर बड़ी बेंच सुनवाई नहीं करेगी. याचिकाकर्ता की मांग थी कि इसे 7 जजों की बेंच को भेजा जाए. आर्टिकल 370 की कानूनी वैधता को सुप्रीम कोर्ट में चुनौती दी गई है. गौरतलब है कि बीते साल पांच अगस्त को केंद्र सरकार ने जम्मू कश्मीर से आर्टिकल 370 को हटा दिया था. इसके बाद विपक्ष के साथ कई संगठनों ने इसका विरोध करना शुरू कर दिया था. बीते माह यानी 23 जनवरी को जस्टिस एनवी रमन्ना ने इस मुद्दे पर अपना फैसला सुरक्षित रखा था.याचिका का विरोध करते हुए केंद्र ने कहा था कि जम्मू-कश्मीर से विशेष राज्य का दर्जा वापस लेने के अलावा और कोई विकल्प नहीं बचा था. एनजीओ पीपुल्स यूनियन ऑफ सिविल लिबर्टीज , जम्मू और कश्मीर हाई कोर्ट बार एसोसिएशन और हस्तक्षेपकर्ता ने मामले को बड़ी पीठ के पास भेजने के लिए कहा है. उन्होंने यह मांग सर्वोच्च अदालत के दो फैसले के आधार पर की है.'''
#   
# =============================================================================
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

#localhost:5004/get_video?title=महिला कोच ने निक जोनस को याद दिलाया- मैं आपसे 10 साल बड़ी हूं&post_text=बॉलीवुड एक्ट्रेस प्रियंका चोपड़ा के पति अमरीकन गायक निक जोनस एक बार फिर दोनों की उम्र में अंतर को लेकर चर्चा में हैं। एक पॉपुलर मैगजीन ने भी जब यही सवाल पूछा तो एक्ट्रेस ने करारा जवाब देते हुए कहा कि जब पुरुष की उम्र ज्यादा हो तो कोई सवाल नहीं करता , लेकिन महिला ज्यादा उम्र की हो तो सवाल क्यों होते हैं'&full_summary=मुंबई. बॉलीवुड एक्ट्रेस प्रियंका चोपड़ा के पति अमरीकन गायक निक जोनस एक बार फिर दोनों की उम्र में अंतर को लेकर चर्चा में हैं. उनसे एक महिला सिंगिंग कोच ने अपनी उम्र का और निक की उम्र में अंतर बताया. फिर क्या था, प्रियंका का जिक्र तो आना ही था. ये मेजदार बातचीत अमरीका के सिंगिंग रियलिटी शो 'द वायस' में सामने आई.अमरीकी रियलिटी सिंगिंग शो ' द वायस' में पहली बार सिंगिंग कोच के रूप में निक जोनस पहुंचे. उनका ये पहला एपिसोड ही था. एक कंटेस्टेंट की गायकी पर कोच बात कर रहे थे. अचानक एक महिला कोच कैली क्लार्कसन ने निक से कहा,' मैं तुमसे 10 साल बड़ी हूं. मेरी उम्र 37 साल है.' इस पर निक जोनस ने बड़ी चालाकी से जवाब दिया,' मेरी पत्नी प्रियंका भी 37 साल की हैं.' इस पर पूरे शो में हंसी के ठहाके गूंज उठे. शो के एक और कोच ब्लैक शेल्टन ने भी निक का स्वागत इसी तरह से किया था. उन्होंने निक का मजाक बनाते हुए कहा,'मैं शो के नियम जरूर पढूंगा क्योंकि ये मेरा शो है. मुझे पक्का पता नहीं है कि आप द वायस शो के कोच बनने के लिए जरूरी उम्र के हैं की नहीं, लेकिन ये अच्छे से पता है कि आपकी यहां खूब खिंचाई होने वाली है.' इस के जवाब में निक ने कहा, कम उम्र के बावजूद उनके पास 20 साल का अनुभव है. प्रियंका से भी उनके और निक की उम्र में अंतर को लेकर सवाल किए जाते रहे हैं. एक पॉपुलर मैगजीन ने भी जब यही सवाल पूछा तो एक्ट्रेस ने करारा जवाब देते हुए कहा कि जब पुरुष की उम्र ज्यादा हो तो कोई सवाल नहीं करता, लेकिन महिला ज्यादा उम्र की हो तो सवाल क्यों होते हैं.




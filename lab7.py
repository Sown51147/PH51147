import streamlit as st
import re

class TextCleaner:
   
    def __clean_text(self, text):
        text = re.sub(r'[.,;:!?~!@#$%^&*()]', '', text)  
        return text
   
    def __clean(self, text):
        text = text.lower()  
        text = self.__clean_text(text)  
        text = re.sub(r'\s+', ' ', text).strip()  
        return text
    
    def __tokenize(self, text):
        words = text.split(' ')
        return words
    
    def __count_words(self, words):
        word_count = {}
        for word in words:
            if word in word_count:
             word_count[word] = word_count[word] + 1
            else:
                word_count[word] = 1
        return word_count
    
    def train(self, spam, not_spam):
        self.spam_word_count = {}
        self.not_spam_word_count = {}
        self.total_spam_words = 0
        self.total_not_spam_words = 0
        self.total_vocab = 0
        
        spam_words = self.__tokenize(spam)
        self.spam_word_count = self.__count_words(spam_words)
        self.total_spam_words = len(spam_words)
        
        not_spam_words = self.__tokenize(not_spam)
        self.not_spam_word_count = self.__count_words(not_spam_words)
        self.total_not_spam_words = len(not_spam_words)
        
        vocab = []
        vocab.extend(self.spam_word_count)
        vocab.extend(self.not_spam_word_count)
        vocab = set(vocab)  
        self.total_vocab = len(vocab)
    
    def phan_loai(self, text):
        text = self.__clean(text)
        words = self.__tokenize(text)
        prob_spam = 0.4
        prob_not_spam = 0.4
        for word in words:
            
            freq_spam = self.spam_word_count.get(word, 0)
            p_spam = (freq_spam + 1) / (self.total_spam_words + self.total_vocab)
            prob_spam = prob_spam * p_spam
           
            freq_not_spam = self.not_spam_word_count.get(word, 0)
            p_not_spam = (freq_not_spam + 1) / (self.total_not_spam_words + self.total_vocab)
            prob_not_spam = prob_not_spam * p_not_spam
        
        return "spam" if prob_spam >= prob_not_spam else "not spam"

cleaner = TextCleaner()
spam = 'nhanh tay nhận khuyến mãi 50% giảm giá cho sản phẩm mới nhất của chúng tôi, giảm giá 70% cho khách hàng thân thiết,hỗ trợ trả góp 0% lãi suất cơ hội cuối cùng để nhận ưu đãi này, đừng bỏ lỡ, liên hệ ngay để biết thêm chi tiết'
not_spam = 'chào bạn, hôm nay có cuộc họp quan trọng lúc 3 giờ chiều, vui lòng xác nhận sự tham gia của bạn, cảm ơn bạn đã hợp tác, chúc bạn một ngày tốt lành'
cleaner.train(spam, not_spam)

st.title("PHÂN LOẠI VĂN BẢN SPAM/NON-SPAM")
st.write("Nhập nội dung văn bản cần phân loại:")
lua_chon = st.selectbox("Chọn cách nhập nội dung: (1: Nhập tay, 2: Tải file .txt)", [1, 2])
noi_dung = ""
if lua_chon == 1:
    noi_dung = st.text_area("Nhập nội dung văn bản:")
elif lua_chon == 2:
    file = st.file_uploader("Tải lên file .txt", type=["txt"])
    if file is not None:
        noi_dung = file.read().decode("utf-8")
        st.text_area("Nội dung file:", noi_dung, height=200)

if st.button("Phân loại"):
    if noi_dung.strip() == "":
        st.warning("Vui lòng nhập nội dung hoặc tải file.")
    else:
        the_loai = cleaner.phan_loai(noi_dung)
        st.success(f"Văn bản thuộc thể loại: {the_loai}")
# Captcha Recognition


## Introduction
CAPTCHA stands for Completely Automated Public Turing test to tell Computers and Humans Apart. A typical captcha consists of a distorted test, which a computer program cannot interpret but a human can "hopefully" still read. Many researchers have started investigating automated methods to solve CAPTCHAs,However it harder to solve newer versions ,where letters are skewed and overlapped. This project aim to decaptcha hard captcha using convolutional neural network (CNN)


![amazon captcha ](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjy75SIrpzmAhUIxIUKHQGbAEgQjRx6BAgBEAQ&url=%2Furl%3Fsa%3Di%26rct%3Dj%26q%3D%26esrc%3Ds%26source%3Dimages%26cd%3D%26ved%3D2ahUKEwjH5ZOCrpzmAhWp34UKHa6iCQgQjRx6BAgBEAQ%26url%3Dhttps%253A%252F%252Fbaymard.com%252Fblog%252Fcaptchas-in-checkout%26psig%3DAOvVaw08eem_xNvadPT8ICtH_Dwc%26ust%3D1575561470357609&psig=AOvVaw08eem_xNvadPT8ICtH_Dwc&ust=1575561470357609)

## Dataset
- [CAPTCHAS](https://www.researchgate.net/publication/248380891_captcha_dataset)​(​more than 1000 captcha images )
each image contain 5 letters word that can contain numbers

## Approach
The idea is to first remove background noise or any random lines then preform character segmentation and labeling. after that train CNN model. finally comes recognition 

## Evaluation 
Classification Accuracy

## Challenges
The project has to deal with the following :
- Inclination of the captcha to the left or right
- Distortion of numbers and letters
- Background noise 
- Character separation

### Github Account
- [BodorAl](https://github.com/Bodoral?tab=repositories)

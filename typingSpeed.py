from threading import Timer
import random
paragraphs=["Plasma is the largest part of your blood. It makes up more than half (about 55%) of its overall content. When separated from the rest of the blood, plasma is a light yellow liquid. Plasma carries water, salts and enzymes. The main role of plasma is to take nutrients, hormones, and proteins to the parts of the body that need it. Cells also put their waste products into the plasma. The plasma then helps remove this waste from the body. Blood plasma also carries all parts of the blood through your circulatory system.","Get a head start on your coding by leveraging Docker images to efficiently develop your own unique applications on Windows and Mac.  Create your multi-container application using Docker Compose. Integrate with your favorite tools throughout your development pipeline Docker works with all development tools you use including VS Code, CircleCI and GitHub.Package applications as portable container images to run in any environment consistently from on-premises Kubernetes to AWS ECS, Azure ACI, Google GKE and more","In 2015's Life Is Strange, Max Caulfield is portrayed with the ability to rewind time to supplement the game's core gameplay mechanism While the lead character rewinds time, visual effects such as post-processing, double exposure, and overlapping screen space particles were employed as an artistic approach to be portrayed The character were created using well-known archetypes, initially to establish a player access point and subsequently to subvert them. The supernatural elements were developed as a metaphor for the character's inner turmoil in order to serve the realism, and specialists were engaged to tackle the subject of teen suicide","ChatGPT (Generative Pre-trained Transformer) was fine-tuned on top of GPT-3.5 using supervised learning as well as reinforcement learning. Both approaches used human trainers to improve the model's performance. In the case of supervised learning the model was provided with conversations in which the trainers played both sides: the user and the AI assistant. In the reinforcement step, human trainers first ranked responses that the model had created in previous conversation. These rankings were used to create 'reward models' that the model was further fine-tuned on using several iterations of Proximal Policy Optimization (PPO). Proximal Policy Optimization algorithms present a cost-effective benefit to trust region policy optimization algorithms; they negate many of the computationally expensive operations with faster performance."]
para=random.choice(paragraphs)
print(para)
#do time limited input
timeout=30
t=Timer(timeout,lambda: print(print(),"Time up. Press Enter to display the results"))
t.start()
n=input("Enter the above paragraph: ")
t.cancel()
wpm=0
para=list(para.split())
n=list(n.split())
for i in range(len(n)):
    if(para[i]==n[i]):
        wpm+=1
print("Your typing speed is",wpm*2,"wpm")
def amazon_faq_bot():
    print("Welcome to Amazon FAQ Bot! Ask me anything about Amazon shopping.")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ").lower()

        if 'prime' in user_input:
            print("Bot: Amazon Prime is a subscription service offering free shipping, streaming, and more.")
        
        elif 'track' in user_input or 'order' in user_input:
            print("Bot: To track your order, go to 'Your Orders' on Amazon and click 'Track package'.")
        
        elif 'return' in user_input:
            print("Bot: To return an item, visit 'Your Orders', select the item, and follow the return steps.")
        
        elif 'cancel' in user_input:
            print("Bot: You can cancel your order by going to 'Your Orders' and clicking 'Cancel items'.")
        
        elif 'payment' in user_input or 'methods' in user_input:
            print("Bot: Amazon accepts credit/debit cards, Amazon Pay, and gift cards.")

        elif user_input == 'exit':
            print("Bot: Goodbye!")
            break
        
        else:
            print("Bot: Sorry, I don't understand. Please ask a different question.")
            

# Run the chatbot
amazon_faq_bot()

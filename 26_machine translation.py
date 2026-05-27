from transformers  import pipeline

translator  = pipeline ("translation_en_to_fr" )

result = translator ("Natural Language Processing is amazing." )
print(result[0]['translation_text' ])
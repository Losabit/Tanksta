from utils.function import *
from utils.PdfCreator import PDF
from utils.ModelFunctions import *
from myconfig import *
CUDA_VISIBLE_DEVICES=""

if __name__ == '__main__':
    code, files_paths = getFunctFromFile(os.path.dirname(os.path.abspath(__file__)))
    codeArray = createCodeAndSummarize(code)
    function_index = 0
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.startPageNums()
    # pdf.add_page()

    y = np.zeros(len(code))
    test = prepare_dataset(code, y)
    model = create_base_model(add_mlp_layers2, encoder)
    model.load_weights(os.path.dirname(os.path.abspath(__file__))+'/model/mlp2')

    valu, label = next(iter(test))
    predicts = model.predict(valu)

    for file_path in files_paths:
        pdf.add_path(file_path[0])
        for i in range(function_index, function_index + file_path[1]):
            print(predicts[function_index])
            if predicts[function_index] > 0.502:
                pdf.add_error("Possible memory error in this function")
            pdf.add_function(codeArray[function_index])
            function_index += 1

    pdf.insertTOC()
    pdf_path = ''.join(os.path.dirname(os.path.abspath(__file__)).split(IGNORE_DIR_NAME)[0]) + 'output/'
    pdf.save(pdf_path, pdf_name)
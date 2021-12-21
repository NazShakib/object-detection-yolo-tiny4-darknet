import fiftyone as fo
import fiftyone.zoo as foz
import json

#dataset = foz.load_zoo_dataset("coco-2017")

def segmentation_remove(filePath):
    try:
        with open(filePath,"r") as file:
            data = json.load(file)
            data_len = len(data["annotations"])
        
        annotations_array = []
        for key in range(data_len):
            annotations = data["annotations"][key]
            if annotations["category_id"]==49 or annotations["category_id"]==87:
                annotations_array.append(annotations)

        data["annotations"] = annotations_array
        with open(filePath,'w') as fileWrite:
            json.dump(data,fileWrite,indent=4)
        print("updated annotations successfully...\n")

    except Exception as e:
        print(e)
    


dataset = foz.load_zoo_dataset(
    "coco-2017",
    split="train",
    label_types=["detections"],
    classes=["knife", "scissors"],
    max_samples=3000,
)
dataset.name = "coco-2017-train"
dataset.persistent = True
print(dataset)
segmentation_remove("C:\\Users\\BS-541\\fiftyone\\coco-2017\\train\\labels.json")

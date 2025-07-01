using UnityEngine;
using UnityEngine.EventSystems;

public class ButtonHold : MonoBehaviour,
IPointerDownHandler, IPointerUpHandler
{
    public bool press = false;

    public void OnPointerUp(PointerEventData ed){
        press = false;
    }

    public void OnPointerDown(PointerEventData ed){
        press = true;
    }
}

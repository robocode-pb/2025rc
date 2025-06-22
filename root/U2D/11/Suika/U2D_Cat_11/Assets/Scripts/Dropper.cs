using System.Collections;
using System.Collections.Generic;
using UnityEngine;
public class Dropper : MonoBehaviour
{
    private GameManager game;
    public GameObject currentFruit;
    private bool hasFruit = false;

    void Start()
    {
        game = GameObject.Find("GameManager").GetComponent<GameManager>();
        
        currentFruit = game.InstantiateFruit(this.transform.position, 0);
        currentFruit.GetComponent<Rigidbody2D>().gravityScale = 0;
        
    }

    public void SpawnNewFruit()
    {
        int randomFruit = Random.Range(0, 5);
        currentFruit = game.InstantiateFruit(this.transform.position, randomFruit);
        currentFruit.GetComponent<Rigidbody2D>().gravityScale = 0;
    }   

    

    void Update()
    {
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        if (!game.gameOver && mousePos.x < 5.5f && mousePos.x > -5.5f) {
            mousePos.z = 0; // sets z to 0
            mousePos.y = 4.5f; // sets y to 4  
            transform.position = mousePos; // sets dropper position to mouse position
        } 

        if (currentFruit != null && currentFruit.GetComponent<Rigidbody2D>().gravityScale == 0) {
            currentFruit.transform.position = this.transform.position;
        }

        if (!game.gameOver && Input.GetMouseButtonDown(0)) {
            currentFruit.GetComponent<Rigidbody2D>().gravityScale = 1;
        }
    }

}

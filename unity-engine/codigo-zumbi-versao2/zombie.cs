using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Zombie : MonoBehaviour
{
    // Start is called before the first frame update
    public float speed = 0.05f;             // Velocidade
    public float rotationSpeed = 100.0f;    // Para fazer a rotação
    public Animator animator;               // Para fazer a animação
    public bool Walk = false;         // Indicador de caminhada

    void Start()
    {
        animator = GetComponent<Animator>();
    }

    // Update is called once per frame
    void Update()
    {
        float move = Input.GetAxis("Vertical");
        float turn = Input.GetAxis("Horizontal");               // Para girar, rotacionar

        if(move != 0)
        {
            animator.SetBool("Run", true);
            Vector3 movement = transform.forward * move * speed * Time.deltaTime;
            transform.position += movement;
        }
        else{
            animator.SetBool("Run", false);
        }
        if (turn !=0)
        {
            float rotation = turn * rotationSpeed * Time.deltaTime;
            transform.Rotate(0,rotation,0);
        }
         if (Walk)
        {
            animator.SetBool("Walk", true);
            Vector3 movement = transform.forward * speed * Time.deltaTime;
            transform.position += movement;
        }
        else
        {
            animator.SetBool("Walk", false);
    }
    if (Input.GetKeyDown(KeyCode.Space))
        {
            ToggleWalk();
        }

    }

    void ToggleWalk()
    {
        Walk = !Walk;
        animator.SetBool("Walk", Walk);
    }    
}
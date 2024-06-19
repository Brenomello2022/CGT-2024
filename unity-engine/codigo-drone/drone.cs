using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class DroneMovement : MonoBehaviour
{
    public Transform target;  // O destino do drone

    public float speed = 1.0f;  // Velocidade de movimento do drone

    public float rotationSpeed = 5.0f;  // Velocidade de rotação do drone

    public float stoppingDistance = 1.0f;  // Distância mínima do alvo para parar

    void Update()
    {

        MoveToTarget();
        
    }

  void MoveToTarget()
    {
        if (target != null)
        {
            // Calcular a direção para o alvo
            Vector3 direction = (target.position - transform.position).normalized;
            
            // Calcular a distância até o alvo
            float distance = Vector3.Distance(transform.position, target.position);

            // Mover o drone em direção ao alvo se estiver fora da distância mínima
            if (distance > stoppingDistance)
            {
                // Rotacionar o drone para enfrentar o alvo
                Quaternion lookRotation = Quaternion.LookRotation(direction);
                transform.rotation = Quaternion.Slerp(transform.rotation, lookRotation, rotationSpeed * Time.deltaTime);

                // Mover o drone em direção ao alvo
                transform.position += transform.forward * speed * Time.deltaTime;
            }
        }
    }
}
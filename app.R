library(shiny)
library(shinydashboard)

source("ui.R")

sample_data <- data.frame(
  category = rep(c("A", "B", "C"), each = 5),
  month = rep(month.abb[1:5], times = 3),
  value = c(12, 18, 25, 28, 35, 8, 14, 19, 21, 27, 16, 20, 24, 30, 38)
)

server <- function(input, output, session) {
  filtered_data <- reactive({
    if (identical(input$category, "All")) {
      return(sample_data)
    }

    sample_data[sample_data$category == input$category, ]
  })

  output$total_box <- renderValueBox({
    valueBox(
      value = sum(filtered_data()$value),
      subtitle = "Total value",
      icon = icon("chart-line")
    )
  })

  output$growth_box <- renderValueBox({
    data <- filtered_data()
    growth <- tail(data$value, 1) - head(data$value, 1)

    valueBox(
      value = growth,
      subtitle = "Sample growth",
      icon = icon("arrow-up")
    )
  })

  output$status_box <- renderValueBox({
    valueBox(
      value = "OK",
      subtitle = "Dashboard status",
      icon = icon("check-circle")
    )
  })

  output$sample_plot <- renderPlot({
    data <- filtered_data()

    par(
      bg = app_colors$chart_bg,
      col.axis = app_colors$chart_axis_text,
      col.lab = app_colors$chart_axis_text,
      col.main = app_colors$chart_title_text
    )

    barplot(
      height = data$value,
      names.arg = paste(data$category, data$month),
      col = app_colors$chart_bar,
      border = app_colors$chart_border,
      las = 2,
      main = "Sample values",
      ylab = "Value"
    )
  })

  output$sample_summary <- renderTable({
    aggregate(value ~ category, data = filtered_data(), FUN = sum)
  })

  output$sample_table <- renderTable({
    filtered_data()
  })
}

shinyApp(ui = ui, server = server)
